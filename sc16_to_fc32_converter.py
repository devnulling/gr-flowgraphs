#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Sc16 To Fc32 Converter
# GNU Radio version: 3.7.14.0
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class sc16_to_fc32_converter(gr.top_block):

    def __init__(self, samp_rate=40e6, input_file="samples.sc16", output_file="samples.sc16"):
        gr.top_block.__init__(self, "Sc16 To Fc32 Converter")

        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate
        self.input_file = input_file
        self.output_file = output_file

        ##################################################
        # Blocks
        ##################################################
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1.0/2**15, ))
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_int*1, input_file, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, output_file, False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_file_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_input_file(self):
        return self.input_file

    def set_input_file(self, input_file):
        self.input_file = input_file
        self.blocks_file_source_0.open(self.input_file, False)

    def get_output_file(self):
        return self.output_file

    def set_output_file(self, output_file):
        self.output_file = output_file
        self.blocks_file_sink_0.open(self.output_file)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(40e6),
        help="Set samp_rate [default=%default]")
    parser.add_option(
        "", "--input-file", dest="input_file", type="string", default="samples.sc16",
        help="Set input_file [default=%default]")
    parser.add_option(
        "", "--output-file", dest="output_file", type="string", default="samples.sc16",
        help="Set output_file [default=%default]")
    return parser


def main(top_block_cls=sc16_to_fc32_converter, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(samp_rate=options.samp_rate, input_file=options.input_file, output_file=options.output_file)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
