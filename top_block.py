#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Apr 10 13:23:33 2020
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.audio_rate = audio_rate = 48000
        self.usb_on = usb_on = True
        self.samp_rate = samp_rate = audio_rate*40
        self.q_offset = q_offset = 0
        self.phase = phase = 0
        self.magnitude = magnitude = -0.1
        self.lsb_on = lsb_on = True
        self.i_offset = i_offset = 0
        self.center_freq = center_freq = 432125000

        ##################################################
        # Blocks
        ##################################################
        self._usb_on_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.usb_on,
        	callback=self.set_usb_on,
        	label='USB',
        	true=True,
        	false=False,
        )
        self.GridAdd(self._usb_on_check_box, 4, 4, 1, 1)
        self._lsb_on_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.lsb_on,
        	callback=self.set_lsb_on,
        	label='LSB',
        	true=True,
        	false=False,
        )
        self.GridAdd(self._lsb_on_check_box, 4, 3, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=center_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=4096,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=audio_rate,
                taps=None,
                fractional_bw=None,
        )
        _q_offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._q_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_q_offset_sizer,
        	value=self.q_offset,
        	callback=self.set_q_offset,
        	label='DC offset Q',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._q_offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_q_offset_sizer,
        	value=self.q_offset,
        	callback=self.set_q_offset,
        	minimum=-0.1,
        	maximum=0.1,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_q_offset_sizer, 3, 0, 1, 7)
        _phase_sizer = wx.BoxSizer(wx.VERTICAL)
        self._phase_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_phase_sizer,
        	value=self.phase,
        	callback=self.set_phase,
        	label='Phase correction',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._phase_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_phase_sizer,
        	value=self.phase,
        	callback=self.set_phase,
        	minimum=-0.1,
        	maximum=0.1,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_phase_sizer, 0, 0, 1, 7)
        _magnitude_sizer = wx.BoxSizer(wx.VERTICAL)
        self._magnitude_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_magnitude_sizer,
        	value=self.magnitude,
        	callback=self.set_magnitude,
        	label='Magnitude correction',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._magnitude_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_magnitude_sizer,
        	value=self.magnitude,
        	callback=self.set_magnitude,
        	minimum=-0.1,
        	maximum=0.1,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_magnitude_sizer, 1, 0, 1, 7)
        _i_offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._i_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_i_offset_sizer,
        	value=self.i_offset,
        	callback=self.set_i_offset,
        	label='DC offset I',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._i_offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_i_offset_sizer,
        	value=self.i_offset,
        	callback=self.set_i_offset,
        	minimum=-0.1,
        	maximum=0.1,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_i_offset_sizer, 2, 0, 1, 7)
        self.blocks_multiply_xx_4 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.band_pass_filter_0_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, -6000, -200, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, 200, 6000, 200, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_4 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 0, 1, 0)
        self.analog_sig_source_x_3_0 = analog.sig_source_c(audio_rate, analog.GR_COS_WAVE, 11000, 1.8 if lsb_on else 0, 0)
        self.analog_sig_source_x_3 = analog.sig_source_c(audio_rate, analog.GR_COS_WAVE, 25000, 1.8 if usb_on else 0, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 5000, 5, 1.0472)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 4000, 2, 0.7854)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 3000, 3, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 2000, 1, 1.5708)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_multiply_xx_3, 1))
        self.connect((self.analog_sig_source_x_3_0, 0), (self.blocks_multiply_xx_3_0, 1))
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_multiply_xx_4, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_3, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_3_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_3, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_3_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_4, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_multiply_xx_4, 0))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_samp_rate(self.audio_rate*40)
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.audio_rate, -6000, -200, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.audio_rate, 200, 6000, 200, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_3_0.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.audio_rate)

    def get_usb_on(self):
        return self.usb_on

    def set_usb_on(self, usb_on):
        self.usb_on = usb_on
        self._usb_on_check_box.set_value(self.usb_on)
        self.analog_sig_source_x_3.set_amplitude(1.8 if self.usb_on else 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_q_offset(self):
        return self.q_offset

    def set_q_offset(self, q_offset):
        self.q_offset = q_offset
        self._q_offset_slider.set_value(self.q_offset)
        self._q_offset_text_box.set_value(self.q_offset)

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        self._phase_slider.set_value(self.phase)
        self._phase_text_box.set_value(self.phase)

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
        self._magnitude_slider.set_value(self.magnitude)
        self._magnitude_text_box.set_value(self.magnitude)

    def get_lsb_on(self):
        return self.lsb_on

    def set_lsb_on(self, lsb_on):
        self.lsb_on = lsb_on
        self._lsb_on_check_box.set_value(self.lsb_on)
        self.analog_sig_source_x_3_0.set_amplitude(1.8 if self.lsb_on else 0)

    def get_i_offset(self):
        return self.i_offset

    def set_i_offset(self, i_offset):
        self.i_offset = i_offset
        self._i_offset_slider.set_value(self.i_offset)
        self._i_offset_text_box.set_value(self.i_offset)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
