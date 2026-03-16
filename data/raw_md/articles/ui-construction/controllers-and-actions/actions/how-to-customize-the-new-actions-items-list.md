---
uid: "112915"
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t326296/how-to-remove-or-hide-the-base-class-from-the-new-action-s-items-list
  altText: How to remove or hide the base class from the New Action's items list
- linkId: DevExpress.ExpressApp.XafApplication.FindListViewId(System.Type)
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.Data
title: "How to: Customize the New Action's Items List"
owner: Ekaterina Kiseleva
---
# How to: Customize the New Action's Items List

This topic demonstrates how to access the list of [business classes](xref:113664) added to the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) items list in WinForms applications.

Generally, you can use the [NewObjectViewController.NewObjectActionItemListMode](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectActionItemListMode) property to choose the predefined mode of populating the New Action item list.   If modes listed in the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectActionItemListMode) enumeration do not fit your requirements, proceed to see how to populate the list manually.

To customize the New Action's Items list, handle the [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) and [NewObjectViewController.CollectCreatableItemTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes) events of the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController), which contains the **New** Action. The former event is raised when the current object type and its descendants are added to the Action's Items list, and the latter is raised when all the remaining types whose **CreatableItem** property is set to **true** in the Application Model (see [](xref:DevExpress.ExpressApp.Model.IModelBOModel)) are added. In the example below, the **Task** item is removed.

In ASP.NET Core Blazor, this Controller hides the **New** Action from the **Task** Views.  

# [CustomizeNewActionItemsListController.cs](#tab/tabid-csharpCustomizeNewActionItemsListController-cs)

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.SystemModule;

namespace CustomizeNewActionItemsListExample.Module.Controllers {
    public class CustomizeNewActionItemsListController : ObjectViewController<ObjectView, Task> {
        protected override void OnActivated() {
            base.OnActivated();
            NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
            if (controller != null) {
                controller.CollectCreatableItemTypes += NewObjectViewController_CollectCreatableItemTypes;
                controller.CollectDescendantTypes += NewObjectViewController_CollectDescendantTypes;
                if (controller.Active) {
                    controller.UpdateNewObjectAction();
                }
            }
        }
        private void NewObjectViewController_CollectDescendantTypes(object sender, CollectTypesEventArgs e) {
            CustomizeList(e.Types);
        }
        private void NewObjectViewController_CollectCreatableItemTypes(object sender, CollectTypesEventArgs e) {
            CustomizeList(e.Types);
        }
        private void CustomizeList(ICollection<Type> types) {
            List<Type> unusableTypes = new List<Type>();
            foreach (Type item in types) {
                if (item == typeof(Task)) {
                    unusableTypes.Add(item);
                }
            }
            foreach (Type item in unusableTypes) {
                types.Remove(item);
            }
        }
        protected override void OnDeactivated() {
            NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
            if (controller != null) {
                controller.CollectCreatableItemTypes -= NewObjectViewController_CollectCreatableItemTypes;
                controller.CollectDescendantTypes -= NewObjectViewController_CollectDescendantTypes;
            }
            base.OnDeactivated();   
        }
    }
 }
```
***
