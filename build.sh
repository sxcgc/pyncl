
$PYTHON setup.py install
cp -r $RECIPE_DIR/src/TPBoundary_3000/ $PREFIX/share
cd $RECIPE_DIR/src/inout
f2py sub.f sg_tools.f dmapgci.f icfell.f icloem.f eprin.f -h cgc_tools.pyf -m cgc_tools --overwrite-signature
f2py -c cgc_tools.pyf sub.f sg_tools.f dmapgci.f icfell.f icloem.f eprin.f
cp cgc_tools*.so $PREFIX/lib/python3.*/lib-dynload/

