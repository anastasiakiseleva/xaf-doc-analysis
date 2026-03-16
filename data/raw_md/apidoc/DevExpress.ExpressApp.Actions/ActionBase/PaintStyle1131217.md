---
uid: DevExpress.ExpressApp.Actions.ActionBase.PaintStyle
name: PaintStyle
type: Property
summary: Specifies the [Action](xref:112622)'s paint style.
syntax:
  content: |-
    [DefaultValue(ActionItemPaintStyle.Default)]
    public ActionItemPaintStyle PaintStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.ActionItemPaintStyle
    description: An [](xref:DevExpress.ExpressApp.Templates.ActionItemPaintStyle) enumeration value that specifies the Action's paint style.
seealso: []
---
Use one of the following approaches to specify this property:

* **In code**
    # [C#](#tab/tabid-csharp)
    
    ```csharp{13}
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp.Templates;
    using DevExpress.Persistent.Base;
    // ...
    public class MyController : ObjectViewController<ListView, Contact> {
        public MyController() {
            SimpleAction customAction = new SimpleAction(this, "CustomAction", PredefinedCategory.View) {
                Caption = "Custom Action",
                ImageName = "ModelEditor_Application"
            };
            customAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
            customAction.PaintStyle = ActionItemPaintStyle.Caption;
        }
    }
    ```
    ***
* **In the Model Editor**  
    Navigate to an [!include[Node_Action](~/templates/node_action111373.md)] node and specify the [IModelAction.PaintStyle](xref:DevExpress.ExpressApp.Model.IModelAction.PaintStyle) property. 

    ![PlainStyle property in Model Editor](~/images/PaintStyle_ModelEditor.png)
    
Note that the value specified in the Model Editor has a higher priority than the value specified in code. For more information, refer to the following topic: [Application Model Basics](xref:112580).
