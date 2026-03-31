---
uid: "403533"
title: Change View UI and Bypass Application Model Updates
---
# Change View UI and Bypass Application Model Updates

This topic explains how to change the View UI in such a way that the modifications don't persist between application runs.

 You can change View settings in code. Users can re-arrange elements while they use the application. XAF saves all these changes as [Model Differences](xref:112580). On every app startup, it loads these differences so that users can continue with the same UI they saw during the last application run.
 
 You can force XAF not to save the **Model Differences**: apply changes in a way that bypasses the [Application Model](xref:112579). The application will then revert changes to UI elements on next startup.

 ## Apply Changes Directly to UI Controls

The following code shows how to modify the UI and keep the **Application Model** unchanged. Access the properties of underlying UI controls directly. Do not use **Application Model** settings (such as [ViewItem.Caption](xref:DevExpress.ExpressApp.Editors.ViewItem.Caption)).

# [C#](#tab/tabid-csharp)

```csharp{17,23-24}
using DevExpress.ExpressApp;
using YourSolutionName.Module.BusinessObjects;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.ExpressApp.Editors;
using DevExpress.XtraEditors;

namespace YourSolutionName.Module.Win.Controllers {
    public class CustomWinController : ObjectViewController<DetailView,Contact> {    
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl(this, CustomizeViewItem_Direct, "myStaticText1");
        }

        // This code saves the changes to the Application Model.
        private void CustomizeViewItem_AppModel(ViewItem viewItem) {
            var item = (StaticTextViewItem)viewItem;
            item.Text = "Saved in the Application Model";
        }

        // This code bypasses the Application Model.
        private void CustomizeViewItem_Direct(ViewItem viewItem) {
            var item = (StaticTextViewItem)viewItem;
            var labelControl =(LabelControl) item.Control;
            labelControl.Text = "Reset on Next Startup";
        }
    }
}
```
***

## Write an Event Handler: Save or Discard Application Model Changes 

Handle the [View.ModelSaving](xref:DevExpress.ExpressApp.View.ModelSaving) event. You can use its parameter to specify whether changes need to be saved or discarded. 

Use cases for this event: 

* Centralized control over Application Model changes 
* Handle changes made by end users

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using dxT941118.Module.BusinessObjects;

namespace dxT941118.Module.Win.Controllers {
    public class CustomWinController : ObjectViewController<DetailView, Contact> {
        protected override void OnActivated() {
            base.OnActivated();
            View.ModelSaving += View_ModelSaving;
        }

        private void View_ModelSaving(object sender, System.ComponentModel.CancelEventArgs e) {
            e.Cancel = true;
        }
    }
}
```
***
