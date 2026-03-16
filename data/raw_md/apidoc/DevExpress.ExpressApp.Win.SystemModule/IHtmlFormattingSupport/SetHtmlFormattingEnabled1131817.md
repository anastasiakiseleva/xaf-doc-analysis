---
uid: DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport.SetHtmlFormattingEnabled(System.Boolean)
name: SetHtmlFormattingEnabled(Boolean)
type: Method
summary: Enables or disables HTML Formatting of the display text.
syntax:
  content: void SetHtmlFormattingEnabled(bool htmlFormattingEnabled)
  parameters:
  - id: htmlFormattingEnabled
    type: System.Boolean
    description: '**true** to enable HTML formatting of the display text; otherwise **false**.'
seealso: []
---
When this method is called with **true** as the argument, it must set the control's text display mode to "HTML-formatted". Otherwise, it must set the control's text display mode to "plain".