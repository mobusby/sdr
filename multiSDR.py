#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MultiSDR
# Author: Mark Busby <mark@BusbyCreations.com>
# Description: Multiple SDRs, multiple demodulators, multiple output paths
# Generated: Mon May 15 21:12:01 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rxAM_3 import rxAM_3  # grc-generated hier_block
from rxNBFM import rxNBFM  # grc-generated hier_block
import osmosdr
import sip
import time
from gnuradio import qtgui


class multiSDR(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MultiSDR")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MultiSDR")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "multiSDR")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.center_freq_ = center_freq_ = 462.5625
        self.samp_rate = samp_rate = 2.4e6
        self.outGain_ = outGain_ = 2
        self.inputGain_ = inputGain_ = 1
        self.filterWidth_ = filterWidth_ = 100
        self.channel_freq_rxFM_2_ = channel_freq_rxFM_2_ = center_freq_
        self.channel_freq_rxFM_1_ = channel_freq_rxFM_1_ = center_freq_
        self.channel_freq_rxAM_ = channel_freq_rxAM_ = center_freq_
        self.sdrGain = sdrGain = inputGain_
        self.resamplerDecimation = resamplerDecimation = 8
        self.outGain = outGain = outGain_
        self.mute_rxFM_2_ = mute_rxFM_2_ = False
        self.mute_rxFM_1_ = mute_rxFM_1_ = False
        self.mute_rxAM_ = mute_rxAM_ = False
        self.filterWidth = filterWidth = 1000*filterWidth_
        self.filterDecimation = filterDecimation = 10
        self.channel_freq_rxFM_2 = channel_freq_rxFM_2 = 1e6*channel_freq_rxFM_2_
        self.channel_freq_rxFM_1 = channel_freq_rxFM_1 = 1e6*channel_freq_rxFM_1_
        self.channel_freq_rxAM = channel_freq_rxAM = 1e6*channel_freq_rxAM_
        self.center_freq = center_freq = 1e6*center_freq_
        self.bandwidth = bandwidth = samp_rate
        self.audioRate = audioRate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.tabWidget0 = Qt.QTabWidget()
        self.tabWidget0_widget_0 = Qt.QWidget()
        self.tabWidget0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabWidget0_widget_0)
        self.tabWidget0_grid_layout_0 = Qt.QGridLayout()
        self.tabWidget0_layout_0.addLayout(self.tabWidget0_grid_layout_0)
        self.tabWidget0.addTab(self.tabWidget0_widget_0, 'Input')
        self.tabWidget0_widget_1 = Qt.QWidget()
        self.tabWidget0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabWidget0_widget_1)
        self.tabWidget0_grid_layout_1 = Qt.QGridLayout()
        self.tabWidget0_layout_1.addLayout(self.tabWidget0_grid_layout_1)
        self.tabWidget0.addTab(self.tabWidget0_widget_1, 'Processing')
        self.tabWidget0_widget_2 = Qt.QWidget()
        self.tabWidget0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabWidget0_widget_2)
        self.tabWidget0_grid_layout_2 = Qt.QGridLayout()
        self.tabWidget0_layout_2.addLayout(self.tabWidget0_grid_layout_2)
        self.tabWidget0.addTab(self.tabWidget0_widget_2, 'Output')
        self.top_grid_layout.addWidget(self.tabWidget0, 0,0)
        _mute_rxFM_2__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_2__choices = {True: True, False: False}
        self._mute_rxFM_2__choices_inv = dict((v,k) for k,v in self._mute_rxFM_2__choices.iteritems())
        self._mute_rxFM_2__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_2__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_2__choices_inv[i]))
        self._mute_rxFM_2__callback(self.mute_rxFM_2_)
        _mute_rxFM_2__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_2_(self._mute_rxFM_2__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_2__check_box, 4,1)
        _mute_rxFM_1__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_1__choices = {True: True, False: False}
        self._mute_rxFM_1__choices_inv = dict((v,k) for k,v in self._mute_rxFM_1__choices.iteritems())
        self._mute_rxFM_1__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_1__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_1__choices_inv[i]))
        self._mute_rxFM_1__callback(self.mute_rxFM_1_)
        _mute_rxFM_1__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_1_(self._mute_rxFM_1__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_1__check_box, 3,1)
        _mute_rxAM__check_box = Qt.QCheckBox('Mute')
        self._mute_rxAM__choices = {True: True, False: False}
        self._mute_rxAM__choices_inv = dict((v,k) for k,v in self._mute_rxAM__choices.iteritems())
        self._mute_rxAM__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxAM__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxAM__choices_inv[i]))
        self._mute_rxAM__callback(self.mute_rxAM_)
        _mute_rxAM__check_box.stateChanged.connect(lambda i: self.set_mute_rxAM_(self._mute_rxAM__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxAM__check_box, 2,1)
        self._center_freq__range = Range(70, 6000, 0.001, 462.5625, 100)
        self._center_freq__win = RangeWidget(self._center_freq__range, self.set_center_freq_, 'Center Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._center_freq__win, 1,0,1,2)
        self.rxNBFM_0_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_2,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxNBFM_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_1,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxAM_3_0 = rxAM_3(
            rxAM_audioRate=48e3,
            rxAM_channelFreq=channel_freq_rxAM,
            rxAM_freq=center_freq,
            rxAM_gain=outGain,
            rxAM_sampleRate=samp_rate,
        )
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(center_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(30, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	bandwidth, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-0.5, 0.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	bandwidth, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,1)
        self._outGain__range = Range(0, 15, 1, 2, 10)
        self._outGain__win = RangeWidget(self._outGain__range, self.set_outGain_, 'Output Gain [dB]', "counter_slider", float)
        self.tabWidget0_grid_layout_2.addWidget(self._outGain__win, 0,0)
        self._inputGain__range = Range(-10, 10, 1, 1, 2)
        self._inputGain__win = RangeWidget(self._inputGain__range, self.set_inputGain_, 'Gain [dB]', "counter_slider", int)
        self.tabWidget0_grid_layout_0.addWidget(self._inputGain__win, 0,0,1,2)
        self._filterWidth__range = Range(10, 200, 1, 100, 10)
        self._filterWidth__win = RangeWidget(self._filterWidth__range, self.set_filterWidth_, 'WBFM Filter Width [kHz]', "counter_slider", int)
        self.tabWidget0_grid_layout_1.addWidget(self._filterWidth__win, 0,0)
        self._channel_freq_rxFM_2__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_2__win = RangeWidget(self._channel_freq_rxFM_2__range, self.set_channel_freq_rxFM_2_, 'FM2 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_2__win, 4,0)
        self._channel_freq_rxFM_1__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_1__win = RangeWidget(self._channel_freq_rxFM_1__range, self.set_channel_freq_rxFM_1_, 'FM1 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_1__win, 3,0)
        self._channel_freq_rxAM__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxAM__win = RangeWidget(self._channel_freq_rxAM__range, self.set_channel_freq_rxAM_, 'AM Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxAM__win, 2,0)
        self.blocks_wavfile_sink_0_0_0 = blocks.wavfile_sink('C:\\Users\\mobusby\\Desktop\\rxNBFM_2.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('C:\\Users\\mobusby\\Desktop\\rxNBFM_1.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('C:\\Users\\mobusby\\Desktop\\rxAM.wav', 1, audioRate, 16)
        self.blocks_mute_xx_0_1 = blocks.mute_ff(bool(mute_rxFM_2_))
        self.blocks_mute_xx_0_0 = blocks.mute_ff(bool(mute_rxFM_1_))
        self.blocks_mute_xx_0 = blocks.mute_ff(bool(mute_rxAM_))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(audioRate, '', False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_mute_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_mute_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_mute_xx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rxAM_3_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rxNBFM_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rxNBFM_0_0, 0))
        self.connect((self.rxAM_3_0, 0), (self.blocks_mute_xx_0, 0))
        self.connect((self.rxAM_3_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.rxNBFM_0, 0), (self.blocks_mute_xx_0_0, 0))
        self.connect((self.rxNBFM_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.rxNBFM_0_0, 0), (self.blocks_mute_xx_0_1, 0))
        self.connect((self.rxNBFM_0_0, 0), (self.blocks_wavfile_sink_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multiSDR")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_freq_(self):
        return self.center_freq_

    def set_center_freq_(self, center_freq_):
        self.center_freq_ = center_freq_
        self.set_center_freq(1e6*self.center_freq_)
        self.set_channel_freq_rxFM_2_(self.center_freq_)
        self.set_channel_freq_rxFM_1_(self.center_freq_)
        self.set_channel_freq_rxAM_(self.center_freq_)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_bandwidth(self.samp_rate)
        self.rxNBFM_0_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxNBFM_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxAM_3_0.set_rxAM_sampleRate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_outGain_(self):
        return self.outGain_

    def set_outGain_(self, outGain_):
        self.outGain_ = outGain_
        self.set_outGain(self.outGain_)

    def get_inputGain_(self):
        return self.inputGain_

    def set_inputGain_(self, inputGain_):
        self.inputGain_ = inputGain_
        self.set_sdrGain(self.inputGain_)

    def get_filterWidth_(self):
        return self.filterWidth_

    def set_filterWidth_(self, filterWidth_):
        self.filterWidth_ = filterWidth_
        self.set_filterWidth(1000*self.filterWidth_)

    def get_channel_freq_rxFM_2_(self):
        return self.channel_freq_rxFM_2_

    def set_channel_freq_rxFM_2_(self, channel_freq_rxFM_2_):
        self.channel_freq_rxFM_2_ = channel_freq_rxFM_2_
        self.set_channel_freq_rxFM_2(1e6*self.channel_freq_rxFM_2_)

    def get_channel_freq_rxFM_1_(self):
        return self.channel_freq_rxFM_1_

    def set_channel_freq_rxFM_1_(self, channel_freq_rxFM_1_):
        self.channel_freq_rxFM_1_ = channel_freq_rxFM_1_
        self.set_channel_freq_rxFM_1(1e6*self.channel_freq_rxFM_1_)

    def get_channel_freq_rxAM_(self):
        return self.channel_freq_rxAM_

    def set_channel_freq_rxAM_(self, channel_freq_rxAM_):
        self.channel_freq_rxAM_ = channel_freq_rxAM_
        self.set_channel_freq_rxAM(1e6*self.channel_freq_rxAM_)

    def get_sdrGain(self):
        return self.sdrGain

    def set_sdrGain(self, sdrGain):
        self.sdrGain = sdrGain

    def get_resamplerDecimation(self):
        return self.resamplerDecimation

    def set_resamplerDecimation(self, resamplerDecimation):
        self.resamplerDecimation = resamplerDecimation

    def get_outGain(self):
        return self.outGain

    def set_outGain(self, outGain):
        self.outGain = outGain
        self.rxAM_3_0.set_rxAM_gain(self.outGain)

    def get_mute_rxFM_2_(self):
        return self.mute_rxFM_2_

    def set_mute_rxFM_2_(self, mute_rxFM_2_):
        self.mute_rxFM_2_ = mute_rxFM_2_
        self._mute_rxFM_2__callback(self.mute_rxFM_2_)
        self.blocks_mute_xx_0_1.set_mute(bool(self.mute_rxFM_2_))

    def get_mute_rxFM_1_(self):
        return self.mute_rxFM_1_

    def set_mute_rxFM_1_(self, mute_rxFM_1_):
        self.mute_rxFM_1_ = mute_rxFM_1_
        self._mute_rxFM_1__callback(self.mute_rxFM_1_)
        self.blocks_mute_xx_0_0.set_mute(bool(self.mute_rxFM_1_))

    def get_mute_rxAM_(self):
        return self.mute_rxAM_

    def set_mute_rxAM_(self, mute_rxAM_):
        self.mute_rxAM_ = mute_rxAM_
        self._mute_rxAM__callback(self.mute_rxAM_)
        self.blocks_mute_xx_0.set_mute(bool(self.mute_rxAM_))

    def get_filterWidth(self):
        return self.filterWidth

    def set_filterWidth(self, filterWidth):
        self.filterWidth = filterWidth

    def get_filterDecimation(self):
        return self.filterDecimation

    def set_filterDecimation(self, filterDecimation):
        self.filterDecimation = filterDecimation

    def get_channel_freq_rxFM_2(self):
        return self.channel_freq_rxFM_2

    def set_channel_freq_rxFM_2(self, channel_freq_rxFM_2):
        self.channel_freq_rxFM_2 = channel_freq_rxFM_2
        self.rxNBFM_0_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_2)

    def get_channel_freq_rxFM_1(self):
        return self.channel_freq_rxFM_1

    def set_channel_freq_rxFM_1(self, channel_freq_rxFM_1):
        self.channel_freq_rxFM_1 = channel_freq_rxFM_1
        self.rxNBFM_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_1)

    def get_channel_freq_rxAM(self):
        return self.channel_freq_rxAM

    def set_channel_freq_rxAM(self, channel_freq_rxAM):
        self.channel_freq_rxAM = channel_freq_rxAM
        self.rxAM_3_0.set_rxAM_channelFreq(self.channel_freq_rxAM)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.rxNBFM_0_0.set_rxNBFM_freq(self.center_freq)
        self.rxNBFM_0.set_rxNBFM_freq(self.center_freq)
        self.rxAM_3_0.set_rxAM_freq(self.center_freq)
        self.rtlsdr_source_0.set_center_freq(self.center_freq, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)

    def get_audioRate(self):
        return self.audioRate

    def set_audioRate(self, audioRate):
        self.audioRate = audioRate
        self.rxNBFM_0_0.set_rxNBFM_audioRate(self.audioRate)
        self.rxNBFM_0.set_rxNBFM_audioRate(self.audioRate)


def main(top_block_cls=multiSDR, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
