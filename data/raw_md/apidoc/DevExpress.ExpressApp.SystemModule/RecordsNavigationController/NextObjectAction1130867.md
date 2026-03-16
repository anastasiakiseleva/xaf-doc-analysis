---
uid: DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction
name: NextObjectAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s **Next Object** Action.
syntax:
  content: public SimpleAction NextObjectAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **Next Object** Action.
seealso: []
---
Use the **Next Object** Action to navigate to the next object in a collection source. In a List View, this Action selects the next object. In a corresponding Detail View, the Action displays properties of the next object.

ASP.NET Core Blazor

:   ![|Records Navigation Controller Next Object Action in ASP.NET Core Blazor, DevExpress|](~/images/blazorrecordsnavigationcontroller_nextobjectaction.png)

Windows Forms

:   ![|Records Navigation Controller Next Object Action in Windows Forms, DevExpress|](~/images/recordsnavigationcontroller_nextaction_win115938.png)

Use the `MoveToNext` method to handle the **Next Object** Action's `Execute` event.

To customize the Action, handle its `Execute` event or inherit from `DevExpress.ExpressApp.Blazor.SystemModule.BlazorRecordsNavigationController` (ASP.NET Core Blazor) or [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController) (Windows Forms) and override the `MoveToNext` method.

The **Next Object** Action is active when the current List View's editor supports focused row [selection](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType).

The **Next Object** Action is enabled when an object is selected in a List View. When the currently selected object is the last one in the collection, the **Next Object** Action is disabled.

Information on the **Next Object** Action is available in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelActionDesign) node. To access it, use the [Model Editor](xref:112582).

> [!NOTE]
> A @DevExpress.ExpressApp.Editors.ListEditor should implement the `IControlOrderProvider` interface to support the **Next Object** Action.