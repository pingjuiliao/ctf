#!/usr/bin/env python
from pwn import *
from random import randint, seed



color_list = [0x00fe00, 0xfe0000, 0x0000fe, 0x808080, 0xfefe00, 0x00fefe, 0xfe00fe]




def parse_information(data) :
    width_in_pixels = u16(data[6:8])
    height_in_pixels= u16(data[8:0xa])
    width2 = u16(data[0x31a:0x31c])
    height2 = u16(data[0x31c:0x31e])

    gct_flows_for_256_colors_with_resolution = u8(data[0xa])
    num_bytes_of_gce_data_flow = u8(data[0x30f])
    end_of_gce_block = u8(data[0x32c])
    transparent_color_num = u8(data[0x310])
    print "width in pixels : %u (%u)" % (width_in_pixels, width2)
    print "height in pixels: %u (%u)" % (height_in_pixels, height2)
    print "next : %u" % gct_flows_for_256_colors_with_resolution
    print "transparent color %u" % transparent_color_num
    print "GCES"
    print "# of data flow : %u" % num_bytes_of_gce_data_flow
    print "end of gce block : %u" % end_of_gce_block



seed(0)

with open("./redacted-puzzle.gif", "rb") as f :
    s = f.read()
    f.close()

print "original_file"
parse_information(s)

i = 4
s = s[:0xd+i*3] + p32(color_list[randint(0, len(color_list)-1)] )[:3] + s[0x10+i*3:]



#for i in range(0, 255) :
#    color = randint(0, 0xffffff)
#    color_bytes = p32(color)[:3]
#    print "%s - %s" % (hex(0xd + i*3), hex(0x10 + i * 3))
#    s = s[:0xd + i*3] + color_bytes + s[0x10 + i * 3:]


with open("./output.gif", "wb") as out :
    out.write(s)
    out.close()



