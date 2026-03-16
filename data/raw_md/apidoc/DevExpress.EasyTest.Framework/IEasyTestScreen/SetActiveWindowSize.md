---
uid: DevExpress.EasyTest.Framework.IEasyTestScreen.SetActiveWindowSize(System.Drawing.Size)
name: SetActiveWindowSize(Size)
type: Method
summary: Resizes an active window.
syntax:
  content: void SetActiveWindowSize(Size size)
  parameters:
  - id: size
    type: System.Drawing.Size
    description: The active window size.
seealso: []
---
Use the `SetActiveWindowSize` method to set a window size before calling the @DevExpress.EasyTest.Framework.IEasyTestScreen.GetScreenshot method to guarantee that window sizes on the actual and expected screenshots are the same.