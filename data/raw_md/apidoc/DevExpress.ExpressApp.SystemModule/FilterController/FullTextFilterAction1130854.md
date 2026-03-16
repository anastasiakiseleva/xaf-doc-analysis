---
uid: DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction
name: FullTextFilterAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.FilterController)'s **FullTextSearch** [Action](xref:112622).
syntax:
  content: public ParametrizedAction FullTextFilterAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.ParametrizedAction
    description: A [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) object that is the **FullTextSearch** Action.
seealso:
- linkId: "112923"
- linkId: DevExpress.Data.Filtering.CriteriaOperator
---
The **FullTextSearch** Action searches the current [List View](xref:112611)'s objects where persistent properties include individual words from a phrase typed by a user:

ASP.NET Core Blazor
:   ![|Full Text Search in ASP.NET Core Blazor, DevExpress|](~/images/filter-blazor-devexpress.png)

Windows Forms
:   ![|Full Text Search in Windows Forms, DevExpress|](~/images/filters_win_1115953.png)

> [!TIP]
> The **FullTextSearch** Action is also available in lookup List Views with certain settings: [](xref:112925).

The following code snippet accesses the **FullTextFilterAction** and shows an object's [Detail View](xref:112611#detail-view) if the Action returns only one object.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.Persistent.BaseImpl;

// ...
public class FilterActionController : ObjectViewController<ListView, Person> {
    protected override void OnActivated() {
        base.OnActivated();
        FilterController filterController = Frame.GetController<FilterController>();
        if(filterController != null) {
            filterController.FullTextFilterAction.Executed += FullTextFilterAction_Executed;
        }
    }
    private void FullTextFilterAction_Executed(object sender, DevExpress.ExpressApp.Actions.ActionBaseEventArgs e) {
        int count = ((IList)View.CollectionSource.Collection).Count;
        if (count == 1) {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
            Object person = ((IList)View.CollectionSource.Collection)[0];
            e.ShowViewParameters.CreatedView = Application.CreateDetailView(
                objectSpace, objectSpace.GetObject(person));
        }
    }
}

```
***

When the **FullTextSearch** is executed, the Search Criteria Builder generates the `CriteriaOperator` object, which is then assigned to the `FullTextSearchCriteria` item of the List View Collection Source's `Criteria` collection. To generate the criterion, the Builder collects the properties based on the Filter Controller's [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) property value.

The **FullTextSearch** Action splits the search request into separate words (uses whitespace characters as delimiters). The result includes records that contain all these words in an arbitrary order. If you need to find the exact match of the phrase (including spaces), enclose your request in quotation marks ("").

> [!NOTE]
> [!include[FullTextSearchFriendlyKeyNote](~/templates/fulltextsearchfriendlykeynote11178.md)]

The following techniques can be used to modify the default behavior of the **FullTextSearch** Action:

* To modify the approach by which the criterion is created, handle the [FilterController.CustomBuildCriteria](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria) event.
* To provide a custom list of the properties to be used in the generated criterion, handle the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event.
* To perform a search only by the properties that are presented by visible columns in the current List View, set the [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) property to the `FullTextSearchTargetPropertiesMode.VisibleColumns` value.
* To exclude individual properties from the list of the properties to be used in the generated criterion, apply the [](xref:DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute) to them. See the [](xref:DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute) as well.
* To search the word combination typed as the Action's parameter, in each persistent property of the available objects, set the [FilterController.FullTextSearchMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchMode) property to the `SearchMode.SearchInProperty` value.

The **FullTextSearch** Action is active when the target object type is persistent, and the object collection is allowed for filtering. To ascertain why the **FullTextSearch** Action is deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **FullTextSearch** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).