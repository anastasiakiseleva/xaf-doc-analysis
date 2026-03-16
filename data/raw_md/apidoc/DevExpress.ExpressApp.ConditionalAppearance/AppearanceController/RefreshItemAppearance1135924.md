---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance(DevExpress.ExpressApp.View,System.String,System.String,System.Object,System.Object)
name: RefreshItemAppearance(View, String, String, Object, Object)
type: Method
summary: Collects and applies the conditional appearance rules appropriate for the specified UI element.
syntax:
  content: public void RefreshItemAppearance(View view, string itemType, string itemName, object item, object contextObject)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object that is the View in which the target UI element (View Items and Layout Items and Groups) is contained. If the target UI element is an [Action](xref:112622), this View is the one for which it is activated.
  - id: itemType
    type: System.String
    description: A string that is the type of the target UI element whose conditional appearance is about to be refreshed.
  - id: itemName
    type: System.String
    description: A string that is the identifier of the UI element whose conditional appearance is about to be refreshed.
  - id: item
    type: System.Object
    description: A UI element whose conditional appearance is about to be refreshed by applying the appropriate rules.
  - id: contextObject
    type: System.Object
    description: An object that contains the properties whose controls or layout items are about to be refreshed by applying the appropriate rules. When the target item is an Action, the selected object(s) is passed as this parameter.
seealso:
- linkId: "113286"
---
To collect rules appropriate for the target item, this method first scans the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **AppearanceRules** node corresponding to the business object represented by the View passed as the _view_ parameter. To access the list of the rules found, handle the [AppearanceController.CollectAppearanceRules](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CollectAppearanceRules) event. In the event handler, you can declare conditional appearance rules for a particular item dynamically and add them to the rules list returned by the [CollectAppearanceRulesEventArgs.AppearanceRules](xref:DevExpress.ExpressApp.ConditionalAppearance.CollectAppearanceRulesEventArgs.AppearanceRules) event handler parameter.

After rules for the target item are collected, they are reviewed, to leave only those rules that satisfy the following conditions:

* The item passed as the _itemName_ parameter is contained in the [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) list;
* The value passed as the _itemType_ parameter is similar to the [IAppearanceRuleProperties.AppearanceItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.AppearanceItemType) property value;
* The View passed as the _view_ parameter is contained in the [IAppearanceRuleProperties.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Context) list;
* The object passed as the _contextObject_ satisfies the criteria specified by the [IAppearanceRuleProperties.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Criteria) or [IAppearanceRuleProperties.Method](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Method) rule property.

To apply the rules to the target item, an **AppearanceObject** is generated. This object contains a list of the appearances (Enabled, Visible, BackColor, FontColor and FontStyle) to be applied to the target item. These appearances are received by combining all the rules found according to their priority (see [IAppearance.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority)). To access the **AppearanceObject**, handle the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) event and use the [ApplyAppearanceEventArgs.AppearanceObject](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceObject) event handler parameter.

The apply the resulting appearance to the target item, this item should implement any set of the following interfaces:

* [](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat)
* [](xref:DevExpress.ExpressApp.Editors.IAppearanceEnabled)
* [](xref:DevExpress.ExpressApp.Editors.IAppearanceVisibility)

To apply a custom conditional appearance to a particular item, handle the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) event and set the event handler's **Handled** parameter to **true** to avoid applying the prepared appearance.

To customize the applied appearance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event.

The **RefreshItemAppearance** method is called by the View Controllers registered in the Appearance Controller when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method is invoked (see [AppearanceController.RegisterController](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RegisterController(DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance))). In addition, this method is called separately by different View Controllers to apply conditional appearance rules to UI elements in particular situations. You can also call this method, when required, from any View Controller.