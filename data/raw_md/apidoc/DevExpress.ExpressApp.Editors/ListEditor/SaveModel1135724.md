---
uid: DevExpress.ExpressApp.Editors.ListEditor.SaveModel
name: SaveModel()
type: Method
summary: Writes information on a [List Editor](xref:113189)'s control to the [Application Model](xref:112580).
syntax:
  content: public virtual void SaveModel()
seealso:
- linkId: DevExpress.ExpressApp.View.SaveModel
---
Generally, you do not have to call this method. It is called automatically when XAF needs to save model settings.

When implementing a `ListEditor` class' descendant, override this method to save the current settings of a List Editor's control to the [Application Model](xref:112580)'s node specified by the List Editor's [ListEditor.Model](xref:DevExpress.ExpressApp.Editors.ListEditor.Model) property.