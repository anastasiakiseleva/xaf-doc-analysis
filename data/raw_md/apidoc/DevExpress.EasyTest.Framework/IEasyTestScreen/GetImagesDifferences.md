---
uid: DevExpress.EasyTest.Framework.IEasyTestScreen.GetImagesDifferences(System.Drawing.Image,System.Drawing.Image,System.Drawing.Image)
name: GetImagesDifferences(Image, Image, Image)
type: Method
summary: Returns an image that shows the difference between an actual and expected image.
syntax:
  content: Image GetImagesDifferences(Image actualImage, Image expectedImage, Image maskImage = null)
  parameters:
  - id: actualImage
    type: System.Drawing.Image
    description: The actual screenshot.
  - id: expectedImage
    type: System.Drawing.Image
    description: The expected screenshot.
  - id: maskImage
    type: System.Drawing.Image
    defaultValue: "null"
    description: A mask image.
  return:
    type: System.Drawing.Image
    description: The image that shows the difference between an actual and expected image.
seealso: []
---
Use the @DevExpress.EasyTest.Framework.IEasyTestScreen.SetActiveWindowSize(System.Drawing.Size) method to set a window size before calling the @DevExpress.EasyTest.Framework.IEasyTestScreen.GetScreenshot method to guarantee that window sizes on the actual and expected screenshots are the same.