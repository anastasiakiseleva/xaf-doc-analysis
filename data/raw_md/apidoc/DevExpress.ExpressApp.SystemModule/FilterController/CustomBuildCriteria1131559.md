---
uid: DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria
name: CustomBuildCriteria
type: Event
summary: Occurs when the **FullTextSearch** [Action](xref:112622) is executed. Allows you to create a custom **CriteriaOperator** that will be used by the **FullTextSearch** Action, to filter the current [List View](xref:112611).
syntax:
  content: public event EventHandler<CustomBuildCriteriaEventArgs> CustomBuildCriteria
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties
- linkId: DevExpress.Data.Filtering.CriteriaOperator
---
Handle this event if you need to modify the approach by which the **CriteriaOperator** is constructed by the **FullTextSearch** Action. In the event handler, create a custom **CriteriaOperator**, based on the string supplied by the handler's **SearchText** parameter. You can also create a custom **CriteriaOperator**, based on the handler's **SearchTextSearchTextWithEscapeCharacters** property, to prohibit end-users from using wildcard characters. Pass the instantiated **CriteriaOperator** to the **Criteria** parameter. Set the handler's **Handled** parameter to **true**, to indicate that the default criteria generation must not take place. If you do not set the **Handled** parameter to **true**, the criteria generation will be performed via the specially created **SearchCriteriaBuilder** object. The properties included in the criterion are determined by the [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) property, and the **SearchClassOptions** and **SearchMemberOptions** attributes, if they are applied to the target class and its members.

As an alternative to handling this event, you can use a custom Search Criteria Builder, by implementing the **ISearchCriteriaBuilder**. You can also inherit the **SearchCriteriaBuilder** that implements this interface, and exposes useful protected methods. To specify a custom Search Criteria Builder, override the **CreateSearchCriteriaBuilder** method in the **FilterController** class descendant. In this instance, your builder's **BuildCriteria** method will be called to generate the criterion. To use a custom set of properties in the generated criteria, handle the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event, or override the **OnCustomGetFullTextSearchProperties** method.

If you handle the **CustomBuildCriteria** event and set the handler's **Handled** parameter to **true**, the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event is not triggered.

To learn about the **FillTextSearch** Action, refer to the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) property description.