---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance(DevExpress.ExpressApp.Editors.IViewInfo,System.String,System.String,System.Object,System.Object,DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptor)
name: RefreshItemAppearance(IViewInfo, String, String, Object, Object, EvaluatorContextDescriptor)
type: Method
summary: Collects and applies the conditional appearance rules appropriate for the specified UI element with a context descriptor specified.
syntax:
  content: public void RefreshItemAppearance(IViewInfo view, string itemType, string itemName, object item, object contextObject, EvaluatorContextDescriptor evaluatorContextDescriptor)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.Editors.IViewInfo
    description: A [](xref:DevExpress.ExpressApp.View) object that is the View in which the target UI element (View Item, Layout Item or Group) is contained. If the target UI element is an [Action](xref:112622), this View is the one for which it is activated.
  - id: itemType
    type: System.String
    description: A string that is the type of the target UI element whose conditional appearance is about to be refreshed.
  - id: itemName
    type: System.String
    description: A string that is the identifier of the UI element whose conditional appearance is about to be refreshed.
  - id: item
    type: System.Object
    description: An UI element whose conditional appearance is about to be refreshed by applying the appropriate rules.
  - id: contextObject
    type: System.Object
    description: An object that contains the properties whose controls or layout items are about to be refreshed by applying the appropriate rules. When the target item is an Action, the selected object(s) is passed as this parameter.
  - id: evaluatorContextDescriptor
    type: DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptor
    description: An EvaluatorContextDescriptor object that is a context descriptor used for checking whether the context object passed as the _contextObject_ parameter satisfies the criteria specified by a rule's [IAppearanceRuleProperties.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Criteria) property.
seealso: []
---
Override this method when you need to implement a custom appearance refresh of the specified item.