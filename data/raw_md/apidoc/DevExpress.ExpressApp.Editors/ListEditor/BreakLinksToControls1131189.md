---
uid: DevExpress.ExpressApp.Editors.ListEditor.BreakLinksToControls
name: BreakLinksToControls()
type: Method
summary: Removes references to the [](xref:DevExpress.ExpressApp.Editors.ListEditor)'s control and its event handlers.
syntax:
  content: public virtual void BreakLinksToControls()
seealso: []
---
The **BreakLinksToControls** method is used when disposing of the current [List Editor](xref:113189), or replacing it with another List Editor.  Generally, you do not need to use this method. However, in the **ListEditor** class' descendants, you can override it if you need to dispose of the manually allocated resources.