---
uid: DevExpress.ExpressApp.View.LoadModel(System.Boolean)
name: LoadModel(Boolean)
type: Method
summary: Applies the [Application Model](xref:112579) changes to the current View.
syntax:
  content: public void LoadModel(bool createControls)
  parameters:
  - id: createControls
    type: System.Boolean
    description: '**true**, if the View controls are created within the **LoadModel** method, otherwise, **false**.'
seealso:
- linkId: "112810"
---
You can use the **LoadModel** method with the [Frame.SetView](xref:DevExpress.ExpressApp.Frame.SetView*) method to reload the Application Model's changes. Refer to the [How to: Apply Application Model Changes to the Current View Immediately](xref:118592) topic for an example.