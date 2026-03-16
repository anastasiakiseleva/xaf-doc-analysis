---
uid: DevExpress.ExpressApp.Editors.ActionContainerViewItem.BreakLinksToControl(System.Boolean)
name: BreakLinksToControl(Boolean)
type: Method
summary: Unsubscribes from the control's events and, depending on the parameter, also disposes of the control and removes the link to the control.
syntax:
  content: public override void BreakLinksToControl(bool unwireEventsOnly)
  parameters:
  - id: unwireEventsOnly
    type: System.Boolean
    description: '**true** to only unsubscribe from events, **false** to also dispose of the control and remove the link to the control.'
seealso: []
---
This method supports the internal infrastructure. You do not need to call this method manually in most cases.

You can override this method in [](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem) descendants to dispose of custom recourses.