---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo(System.String,System.Boolean,System.String)
name: GetImageInfo(String, Boolean, String)
type: Method
summary: Supplies metadata on a standard-sized image.
syntax:
  content: public ImageInfo GetImageInfo(string imageName, bool isEnabled, string imageFolder)
  parameters:
  - id: imageName
    type: System.String
    description: The image's name.
  - id: isEnabled
    type: System.Boolean
    description: Specifies which image should be returned. If `true`, returns the image with the specified `imageName`. If `false`, returns a monochrome image (not SVG), or looks for the image with the name `imageName_Disabled` (SVG).
  - id: imageFolder
    type: System.String
    description: The name of the folder where the image resides.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: The @DevExpress.ExpressApp.Utils.ImageInfo object.
seealso: []
---
