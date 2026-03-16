---
uid: DevExpress.ExpressApp.Editors.ListEditor.CreateControls
name: CreateControls()
type: Method
summary: Creates the current [List Editor](xref:113189)'s control that represents a List View in a UI.
syntax:
  content: public object CreateControls()
  return:
    type: System.Object
    description: An object which represents the current List Editor's control.
seealso:
- linkId: DevExpress.ExpressApp.Editors.ListEditor.Control
- linkId: DevExpress.ExpressApp.Editors.ListEditor.ControlsCreated
- linkId: DevExpress.ExpressApp.Editors.ListEditor.SaveModel
---
This method is automatically called by a List View when it needs to create its List Editor. For instance, this method is called when a List View is visualized or the Application Model's node which stores the List Editor's settings is changed. Generally, you do not have to call this method manually.

When deriving from the **ListEditor** class, override the protected **CreateControlsCore** method to create a List Editor's control (see [](xref:DevExpress.ExpressApp.Editors.ListEditor)).