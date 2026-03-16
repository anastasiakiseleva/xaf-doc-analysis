---
uid: DevExpress.ExpressApp.SystemModule.FilterController
name: FilterController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **FullTextSearch**  and **SetFilter** [Actions](xref:112622).
syntax:
  content: 'public class FilterController : ViewController, IModelExtender, IFilterActionProvider'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.FilterController._members
  altText: FilterController Members
- linkId: "112923"
- linkId: DevExpress.Data.Filtering.CriteriaOperator
---
The `FilterController` displays the **FullTextSearch** and **SetFilter** Actions.

ASP.NET Core Blazor
:   ![Filter Controller SetFilter Action in ASP.NET Core Blazor, DevExpress](~/images/filtercontroller-filteraction-blazor-devexpress.png)

    ![Filter Controller FullTextSearch Action in ASP.NET Core Blazor, DevExpress](~/images/filtercontroller-filterbytextaction-blazor-devexpress.png)

Windows Forms
:   ![Filter Controller SetFilter Action in Windows Forms, DevExpress](~/images/filtercontroller_filteraction_win115955.png)

    ![Filter Controller FullTextSearch Action in Windows Forms, DevExpress](~/images/filtercontroller_filterbytextaction_win115956.png)

For details on the **FullTextSearch** and **SetFilter** Actions, refer to the description of the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) and [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction) properties, that provide access to these Actions.

To customize the default behavior of the **FullTextSearch** and **SetFilter** Actions, you can inherit from this Controller, or subscribe to its events. In addition, you can access the Actions to modify their behavior.

This Controller does not have platform-specific descendants, and you can create your own descendants to change its behavior. When deriving from the `FilterController`, the following protected virtual methods are available, and can be overridden:

{|
|-

! Method
! When is it called?
! Description
|-

| `SetupFilters`
| Invoked when the `FilterController` is activated.
| Applies the criteria that is set for the current List View's [IModelListView.Criteria](xref:DevExpress.ExpressApp.Model.IModelListView.Criteria) property in the Application Model. In addition, creates items for the **SetFilter** Action using the **ListView** | **Filters** node from the Application Model. Executes the **SetFilter** Action, setting the filter specified by the **Filters** node's `CurrentFilterID` property.
|-

| `ApplyFilter`
| First, it is invoked when the `FilterController` is activated to apply an initial filter. Second, it is invoked when the **SetFilter** Action is executed, to apply the selected filter.
| Generates a CriteriaOperator from the passed criterion, and adds it to the `Criteria` collection of the current List View' CollectionSource.
|-

| `GetToolTip`
| Invoked to generate a tooltip for the **SetFilter** Action. The tooltip is formed from the criteria applied to the current View's collection source.
| * If the **Views** | **View** node defining the current List View has the `Criteria` property set, this method applies the specified criterion via the `ApplyCriteria` method.
* If the **Views** | **View** | **Filters** node exists for the current List View, its child nodes are used to populate the **SetFilter** Action's **Items** collection. The item that is specified by the **Filters** node's `CurrentFilterID` property is set as a selected item (see [SingleChoiceAction.SelectedItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem)), and its criterion is applied to the List View via the `SetFilter` method.
|-

| `SetFilter`
| Invoked as a result of executing the **SetFilter** Action.
| The **SetFilter** Action's [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event handler. Applies the selected filter passed as the `Execute` event handler's parameter, to the current List View, via the `ApplyFilter` method. In addition, it sets the selected filter for the `CurrentFilterID` property of the current View's **Views** | **View** node.
|-

| `FullTextSearch`
| Invoked as a result of executing the **FullTextSearch** Action.
| The **FullTextSearch** Action's [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event handler. Using the `Execute` event arguments, it generates a `CriteriaOperator`, and adds it to the `Criteria` collection of the current List View's CollectionSource. To generate the `CriteriaOperator`, the static `DevExpress.ExpressApp.Filtering.FullTextSearchCriteriaBuilder` class is used.
|-

| `OnCustomBuildCriteria`
| Invoked by the `FullTextSearch` method.
| Raises the [FilterController.CustomBuildCriteria](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria) event. To implement a custom algorithm for building criteria in the `FilterController` class descendant, override this method. Set the `CustomBuildCriteriaEventArgs.Handled` parameter to `true`, to prohibit executing a default algorithm. Assign the generated criteria to the `CustomBuildCriteriaEventArgs.Criteria` parameter.
|-

| `CreateSearchCriteriaBuilder`
| Invoked by the `FullTextSearch` method.
| Creates a `SearchCriteriaBuilder` object to be used for building criteria. Override this method, to return an object of the custom class that implements the `ISearchCriteriaBuilder` interface. Note that in this instance, this object's `BuildCriteria` method will be called to generate the criterion for the current List View.
|-

| `OnCustomGetFullTextSearchProperties`
| Invoked by the `FullTextSearch` method.
| Raises the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event. To collect properties for a search in a custom way in the `FilterController` class descendant, override this method. Set the `CustomGetFullTextSearchPropertiesEventArgs.Handled` parameter to `true` to prohibit collecting the properties in the default manner. Assign the set of the collected properties to the `CustomGetFullTextSearchPropertiesEventArgs.Properties` parameter.
|-

| `RemoveFilter`
| Invoked when the current List View's [ListView.Model](xref:DevExpress.ExpressApp.ListView.Model) property is changed (see [View.ModelChanged](xref:DevExpress.ExpressApp.View.ModelChanged)), to remove the filter specified by the `Criteria` property of the List View's **Views** | **View** node.
| Removes the passed criterion from the `Criteria` collection of the current List View' CollectionSource.
|-

| `UpdateActionState`
| Invoked as a result of changing the environment.
| Checks whether the active or enabled state of the **SetFilter** and **FullTextSearch** Actions should be changed after the environment has been changed.
|}

Public members are described individually in the documentation.

This Controller is activated for [List Views](xref:112611) only. To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information about the `FilterController` and its **SetFilter** and **FullTextSearch** Actions is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).