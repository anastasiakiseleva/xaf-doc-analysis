---
uid: DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction
name: PreviousObjectAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s **Previous Object** Action.
syntax:
  content: public SimpleAction PreviousObjectAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **Previous Object** Action.
seealso: []
---
Use the **Previous Object** Action to navigate to the previous object in the collection source. In a List View, this Action selects the previous object. In a corresponding Detail View, this Action displays properties of the previous object.

ASP.NET Core Blazor

:   ![|Records Navigation Controller Previous Object Action in ASP.NET Core Blazor, DevExpress|](~/images/blazorrecordsnavigationcontroller_previousobjectaction.png)

Windows Forms

:   ![|Records Navigation Controller Previous Object Action in Windows Forms, DevExpress|](~/images/recordsnavigationcontroller_previousaction_win115940.png)

Use the `MoveToPrevious` method to handle the **Previous Object** Action's `Execute` event.

To customize the Action, handle the Action's `Execute` event or inherit from `DevExpress.ExpressApp.Blazor.SystemModule.BlazorRecordsNavigationController` (ASP.NET Core Blazor) or [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController) (Windows Forms) and override the `MoveToPrevious` method.

The **Previous Object** Action is active when the current List View's editor supports focused row [selection](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType).

The **Previous Object** Action is enabled when an object is selected in a List View. When the selected object is the first one in the collection, the **Previous Object** Action is disabled.

Information on the **Previous Object** Action is available in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelActionDesign) node. To access it, use the [Model Editor](xref:112582).

> [!NOTE]
> A @DevExpress.ExpressApp.Editors.ListEditor should implement the `IControlOrderProvider` interface to support the **Previous Object** Action.