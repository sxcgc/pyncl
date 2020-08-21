#
#  File:
#    NglLib
#
#  概要:
#    这是一些pyngl的高级库
#
#  Categories:
#    tickmarks
#    maps
#
#  Author:
#    Mary Haley
#
#  Date of initial publication:
#    July 2011
#
#  Description:
#    This example also shows how to overlay a blank plot on a map.
#
#  Effects illustrated:
#    o  Customizing tickmark labels
#    o  Creating a blank plot
#    o  Overlaying plots
#
#  Output:
#     This example produces two frames: one with the default
#     map tickmarks and one with customized tickmarks.
#

#*************************justMapLabel
# 作用：修改contour map的标尺
#
import Ngl
import numpy as np
import datetime

def nameAsTime():
  time = datetime.datetime.now()
  s = time.strftime("_%Y%m%d")
  return s


def justMapLabel(wks,plot,lon_values,lat_values):

    #
    # Create arrays of labels for the lat tickmark locations.
    # Customize them with 'S' or 'N' as appropriate.
    #
    lat_labels = []
    lon_values = np.array(lon_values)
    lat_values = np.array(lat_values)
    for l in lat_values:
      if l < 0:
        lat_labels.append("{:g}~S~o~N~S".format(abs(l)))
      elif l > 0:
        lat_labels.append("{:g}~S~o~N~N".format(l))
      else:
        lat_labels.append("EQ".format(l))
#
    #
    # Create arrays of labels for the lon tickmark locations.
    # Customize them with 'E' or 'W' as appropriate.
    #
    lon_labels  = []
    for l in lon_values:
      if l < 0:
        lon_labels.append("{:g}~S~o~N~W".format(abs(l)))
      elif l > 0:
        lon_labels.append("{:g}~S~o~N~E".format(l))
      else:
        lon_labels.append("{:g}~S~o~N~".format(l))

    if(np.min(lon_values)<0):
      lon_values = lon_values + 180.0
#
    ##----------------------------------------------------------------------
    ## This section creates a blank plot, for the purpose of customizing
    ## its tickmarks.
    ##----------------------------------------------------------------------
    bres = Ngl.Resources()
    #---Retrieve viewport coordinates and set them for blank plot.
    bres.vpXF      = Ngl.get_float(plot,"vpXF")
    bres.vpYF      = Ngl.get_float(plot,"vpYF")
    bres.vpHeightF = Ngl.get_float(plot,"vpHeightF")
    bres.vpWidthF  = Ngl.get_float(plot,"vpWidthF" )

    #---Retrieve min/max values of map and set them for blank plot.
    bres.trXMinF   = Ngl.get_float(plot,"trXMinF")
    bres.trXMaxF   = Ngl.get_float(plot,"trXMaxF")
    bres.trYMinF   = Ngl.get_float(plot,"trYMinF")
    bres.trYMaxF   = Ngl.get_float(plot,"trYMaxF")

    #---Default is inward.
    bres.nglPointTickmarksOutward = True

    bres.tmXTOn = Ngl.get_integer(plot,"tmXTOn")
    bres.tmYROn = Ngl.get_integer(plot,"tmYROn")
    bres.tmXBLabelsOn = Ngl.get_integer(plot,"tmXBLabelsOn")
    bres.tmYLLabelsOn = Ngl.get_integer(plot,"tmYLLabelsOn")

    #---Set the values and labels for the X axis of blank plot.
    bres.tmXBMode                = "Explicit"

    bres.tmXBValues              = lon_values
    bres.tmXBLabels              = lon_labels
    bres.tmXBLabelFontHeightF    = Ngl.get_float(plot,"tmXBLabelFontHeightF")     # Make labels smaller. This
                                                # will affect Y labels too.

    #---Set the values and labels for the Y axis of blank plot.
    bres.tmYLMode                = "Explicit"
    bres.tmYLValues              = lat_values
    bres.tmYLLabels              = lat_labels
    bres.tmXBMajorLengthF = 0.009


    #---Align four corners of both plots, that is, don't do data transformation
    bres.tfDoNDCOverlay          = True

    #---Create the blank plot.
    blank = Ngl.blank_plot(wks,bres)

    #---Draw blank plot for debugging purposes.
    #Ngl.draw(blank)
    #Ngl.frame(wks)

    #---Overlay blank plot on existing map plot.
    Ngl.overlay(plot.base,blank)
#----------------------------------------------------------------------
# Function to add three subtitles to the top of a plot, left-justified,
# centered, and right-justified.
#----------------------------------------------------------------------
def subtitles(wks, plot, left_string="", center_string="", right_string=""):
  ttres         = Ngl.Resources()
  ttres.nglDraw = False          # Make sure string is just created, not drawn.
#
# Retrieve font height of left axis string and use this to calculate
# size of subtitles.
#
  font_height = Ngl.get_float(plot.base,"tiXAxisFontHeightF")
  ttres.txFontHeightF = font_height*0.8    # Slightly smaller

#
# Set some some annotation resources to describe how close text
# is to be attached to plot.
#
  amres = Ngl.Resources()
  amres.amOrthogonalPosF = -0.55   # Top of plot plus a little extra
                                   # to stay off the border.
#
# Create three strings to put at the top, using a slightly
# smaller font height than the axis titles.
#
  if left_string != "":
    txidl = Ngl.text_ndc(wks, left_string, 0., 0., ttres)

    amres.amJust         = "BottomLeft"
    amres.amParallelPosF = -0.5   # Left-justified
    annoidl              = Ngl.add_annotation(plot, txidl, amres)

  if center_string != "":
    txidc = Ngl.text_ndc(wks, center_string, 0., 0., ttres)

    amres.amJust         = "BottomCenter"
    amres.amParallelPosF = 0.0   # Centered
    annoidc              = Ngl.add_annotation(plot, txidc, amres)

  if right_string != "":
    txidr = Ngl.text_ndc(wks, right_string, 0., 0., ttres)

    amres.amJust         = "BottomRight"
    amres.amParallelPosF = 0.5   # Right-justifed
    annoidr              = Ngl.add_annotation(plot, txidr, amres)

  return
