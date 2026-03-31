---
uid: "118760"
seealso:
- linkId: "112803"
title: 'How to: Create and Show a Detail View of the Selected Object in a Popup Window (ASP.NET Core Blazor)'
---
# How to: Create and Show a Detail View of the Selected Object in a Popup Window (ASP.NET Core Blazor)

This topic demonstrates how to create and show a [Detail View](xref:112611) of the List View's selected object in a pop-up window.

> [!NOTE]
> To follow the steps below, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

1. In the _MainDemo.Blazor.Server\Controllers_ folder, create a new [View Controller](xref:112621).
2. In the Controller, create a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) and handle its [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event as shown in the following code snippet:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.Persistent.Base;

    public class ShowDetailViewController : ViewController<ListView> {
    
        public ShowDetailViewController() {
            // Create am Action that shows a popup window.
            PopupWindowShowAction showDetailViewAction = new PopupWindowShowAction(
                this, "ShowDetailView", PredefinedCategory.Edit);
            // Specify that the Action requires user to select an object.
            showDetailViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
            showDetailViewAction.TargetObjectsCriteria = "Not IsNewObject(This)";
            showDetailViewAction.CustomizePopupWindowParams += showDetailViewAction_CustomizePopupWindowParams;
        }
    
        void showDetailViewAction_CustomizePopupWindowParams(
            object sender, CustomizePopupWindowParamsEventArgs e) {
            // Create an Object Space.
            IObjectSpace newObjectSpace = Application.CreateObjectSpace(View.ObjectTypeInfo.Type);
            // Access the View's current object.
            Object objectToShow = newObjectSpace.GetObject(View.CurrentObject);
            if (objectToShow != null) {
                // Create a new Detail View.
                DetailView createdView = Application.CreateDetailView(newObjectSpace, objectToShow);
                // Pass the created View to the CustomizePopupWindowParams event's parameter.
                e.View = createdView;
            }
        }
    }
    ```
    [`PopupWindowShowAction`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction
    [`CustomizePopupWindowParams`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams
    [`CreateObjectSpace`]: xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*
    [`GetObject`]: xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)
    [`CurrentObject`]: xref:DevExpress.ExpressApp.View.CurrentObject
    [`CreateDetailView`]: xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*
    [`e.View`]: xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View
    [`RequireSingleObject`]: xref:DevExpress.ExpressApp.Actions.SelectionDependencyType

    > [!TIP]
    > You can further customize Detail View properties in the @DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams event handler. For example, you can specify the View's @DevExpress.ExpressApp.View.Caption.

3. Save the changes, build the project, and run the application.

    XAF displays the **Show Detail View** Action in the List View's toolbar and the grid's command column. Click the Action to invoke the selected object's Detail View in a pop-up window.

    ![|XAF ASP.NET Core Blazor Detail View of the Selected Object in a Popup Window, DevExpress](~/images/xaf-blazor-detail-view-in-popup-window-devexpress.gif)

> [!TIP]
> The pop-up window uses a separate Object Space and displays the **Save** Action that allows users to explicitly commit changes. You can use any of the following options to customize this behavior:
>
>    * Call the `CreateDetailView` method overload with the `isRoot` parameter. 
>    * Access a nested or existing Object Space instead of a new one. 
>
>    For more information, refer to the following topic: [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot).
