---
uid: "403527"
title: Change the Application Model
owner: Andrey Kozhevnikov
---
# Change the Application Model

## Use the Model Editor 

The Application Model may set settings on multiple levels. You can examine and edit settings on any level that uses a XAFML file. This includes all layers but level zero (settings generated based on Business Model code).

To edit settings on any of those levels, use the [Model Editor](xref:112582).

![ModelEditorDesign](~/images/modeleditordesign115654.png)

## Get or Set Model Settings in Code  

You can access the Application Model in code and either read or modify the required values.

> [!IMPORTANT]
>Note that the UI does not immediately reflect changes made in the Application Model. If you need to apply changes **after** XAF creates and initializes a UI control, access the control directly. See [](xref:402154) for more information. You can also recreate a control with the latest Application Model changes as described in the following article: [](xref:118592).

To access the Application Model in code, use the following objects:

| Object | Property |
|---|---|
| [](xref:DevExpress.ExpressApp.View) | [View.Model](xref:DevExpress.ExpressApp.View.Model) |
| [](xref:DevExpress.ExpressApp.Actions.ActionBase) | [ActionBase.Model](xref:DevExpress.ExpressApp.Actions.ActionBase.Model) |
| [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) | [PropertyEditor.Model](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Model) |
| [](xref:DevExpress.ExpressApp.XafApplication) | [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) |

These properties return an [](xref:DevExpress.ExpressApp.Model.IModelNode) descendant that encapsulates the corresponding node. You can use the **Application** property to access the Application Model's root node. Refer to the following topic for additional information: [](xref:112580). 

The following code shows how to access the 'Contact' business class and modify its [IModelClass.Caption](xref:DevExpress.ExpressApp.Model.IModelClass.Caption):

# [C#](#tab/tabid-csharp)

```csharp
using System.Linq;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;

namespace YourSolutionName.Module.Controllers {
    public class CustomController : ViewController {
        public CustomController() {
            var myAction1 = new SimpleAction(this, "MyAction1", null);
            myAction1.Execute += MyAction1_Execute;
        }

        private void MyAction1_Execute(object sender, 
         SimpleActionExecuteEventArgs e) {
            var lst = Application.Model.BOModel.ToList();
            var bo = Application.Model.BOModel.Where(x => x.Name == 
             "YourSolutionName.Module.BusinessObjects.Contact").FirstOrDefault();
            if(bo != null) {
                var oldCaption = bo.Caption;
                bo.Caption = "New test caption";
            }
        }
    }
}
```
***

