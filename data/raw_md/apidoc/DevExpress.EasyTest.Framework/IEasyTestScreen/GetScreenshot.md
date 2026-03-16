---
uid: DevExpress.EasyTest.Framework.IEasyTestScreen.GetScreenshot
name: GetScreenshot()
type: Method
summary: Makes a screenshot of an application window.
syntax:
  content: Image GetScreenshot()
  return:
    type: System.Drawing.Image
    description: An application's screenshot.
seealso: []
---
Call the @DevExpress.EasyTest.Framework.IEasyTestScreen.SetActiveWindowSize(System.Drawing.Size) method before calling the `GetScreenshot` method to guarantee that window sizes on the actual and expected screenshots are the same.