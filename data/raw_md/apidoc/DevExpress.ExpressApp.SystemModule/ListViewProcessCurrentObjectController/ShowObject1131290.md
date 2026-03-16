---
uid: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ShowObject(System.Object,DevExpress.ExpressApp.ShowViewParameters,DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.View)
name: ShowObject(Object, ShowViewParameters, XafApplication, Frame, View)
type: Method
summary: Creates a Detail View for the currently selected object.  Assigns the View to the [ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) property of the passed **ShowViewParameters** object.
syntax:
  content: public static void ShowObject(object obj, ShowViewParameters showViewParameters, XafApplication application, Frame sourceFrame, View sourceView)
  parameters:
  - id: obj
    type: System.Object
    description: An object for which a Detail View must be created.
  - id: showViewParameters
    type: DevExpress.ExpressApp.ShowViewParameters
    description: A [](xref:DevExpress.ExpressApp.ShowViewParameters) object used to invoke a Detail View for the specified object.
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object that provides methods and properties to manage the current application.
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    description: A [](xref:DevExpress.ExpressApp.Frame) object that represents the [Frame](xref:112608) whose View contains the specified object.
  - id: sourceView
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object that represents the [View](xref:112611) which contains the specified object.
seealso: []
---
This method is called when the [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) is executed. It creates a Detail View for the specified object. The Detail View is assigned to the **ShowViewParameters** object passed as the _showViewParameters_ parameter. This causes the assigned View to be shown after the Action is executed (see [](xref:DevExpress.ExpressApp.ShowViewParameters)).

An exception is thrown if the specified object is new and the source View is not nested.

If the source View is a read-only nested View, representing an aggregated collection, the created Detail View is set to read-only.

This method is static. You can call it in the **Execute** event handler of your Action, passing the object and ShowViewParameters specified by the event handler's parameters. In this instance, a Detail View for the passed object will be invoked after your Action has been executed.