#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MultiSDR
# Author: Mark Busby <mark@BusbyCreations.com>
# Description: Multiple SDRs, multiple demodulators, multiple output paths
# Generated: Sun Apr  2 13:24:13 2017
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_ = samp_rate_ = 10
        self.samp_rate = samp_rate = 1e6 * samp_rate_
        self.outGain_ = outGain_ = 0
        self.inputGain_ = inputGain_ = 0
        self.center_freq_ = center_freq_ = 98
        self.sdrGain = sdrGain = inputGain_
        self.outGain = outGain = outGain_
        self.center_freq = center_freq = 1e6*center_freq_
        self.bandwidth = bandwidth = samp_rate

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
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("type=b200", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(sdrGain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(bandwidth, 0)
        self._samp_rate__range = Range(1, 50, 2, 10, 200)
        self._samp_rate__win = RangeWidget(self._samp_rate__range, self.set_samp_rate_, 'Sampling Rate => Bandwidth [MHz]', "counter_slider", int)
        self.tabWidget0_grid_layout_0.addWidget(self._samp_rate__win, 1,0)
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
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
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
        self._outGain__range = Range(-20, 20, 1, 0, 10)
        self._outGain__win = RangeWidget(self._outGain__range, self.set_outGain_, 'Output Gain [dB]', "counter_slider", int)
        self.tabWidget0_grid_layout_2.addWidget(self._outGain__win, 0,0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	outGain, samp_rate, 100000, 10000, firdes.WIN_HAMMING, 6.76))
        self._inputGain__range = Range(-20, 20, 1, 0, 2)
        self._inputGain__win = RangeWidget(self._inputGain__range, self.set_inputGain_, 'Gain [dB]', "counter_slider", int)
        self.tabWidget0_grid_layout_0.addWidget(self._inputGain__win, 2,0)
        self._center_freq__range = Range(70, 6000, 1, 98, 10)
        self._center_freq__win = RangeWidget(self._center_freq__range, self.set_center_freq_, 'Center Frequency [MHz]', "counter_slider", int)
        self.tabWidget0_grid_layout_0.addWidget(self._center_freq__win, 0,0)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=48,
        	audio_decimation=(int)(samp_rate/1000),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate_(self):
        return self.samp_rate_

    def set_samp_rate_(self, samp_rate_):
        self.samp_rate_ = samp_rate_
        self.set_samp_rate(1e6 * self.samp_rate_)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_bandwidth(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.outGain, self.samp_rate, 100000, 10000, firdes.WIN_HAMMING, 6.76))

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

    def get_center_freq_(self):
        return self.center_freq_

    def set_center_freq_(self, center_freq_):
        self.center_freq_ = center_freq_
        self.set_center_freq(1e6*self.center_freq_)

    def get_sdrGain(self):
        return self.sdrGain

    def set_sdrGain(self, sdrGain):
        self.sdrGain = sdrGain
        self.uhd_usrp_source_0.set_gain(self.sdrGain, 0)


    def get_outGain(self):
        return self.outGain

    def set_outGain(self, outGain):
        self.outGain = outGain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.outGain, self.samp_rate, 100000, 10000, firdes.WIN_HAMMING, 6.76))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.uhd_usrp_source_0.set_bandwidth(self.bandwidth, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)


def main(top_block_cls=top_block, options=None):

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
