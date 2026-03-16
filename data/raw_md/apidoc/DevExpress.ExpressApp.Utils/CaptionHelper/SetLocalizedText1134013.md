---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.SetLocalizedText(DevExpress.ExpressApp.Model.IModelLocalizationGroup,System.Collections.Generic.IList{System.String},System.Collections.Generic.IList{System.String})
name: SetLocalizedText(IModelLocalizationGroup, IList<String>, IList<String>)
type: Method
summary: Performs a batch update of the [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) property values for the **LocalizationItem** child nodes of a particular **LocalizationGroup** node.
syntax:
  content: public static void SetLocalizedText(IModelLocalizationGroup node, IList<string> itemNames, IList<string> itemValues)
  parameters:
  - id: node
    type: DevExpress.ExpressApp.Model.IModelLocalizationGroup
    description: An [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) object, representing the **LocalizationGroup** node whose **LocalizationItem** child nodes' property values will be updated.
  - id: itemNames
    type: System.Collections.Generic.IList{System.String}
    description: An **IList\<String>** object representing a collection of the **LocalizationItem** node names, for which new values must be assigned to the [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) properties.
  - id: itemValues
    type: System.Collections.Generic.IList{System.String}
    description: An **IList\<String>** object representing values that must be assigned to the [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) properties of the nodes specified by the _itemNames_ parameter.
seealso:
- linkId: "112595"
---
If the **LocalizationItem** node specified by an item in the _itemNames_ list does not exist, it is created.

The [Application Model](xref:112580) has the **Localization** node, which allows [localization](xref:112595) of various constants. The **Localization** node is used to localize custom strings used in an **XAF** application. The node contains **LocalizationGroup** child nodes. Each **LocalizationGroup** child node contains a set of **LocalizationItem** child nodes. The **SetLocalizedText** method allows you to change values of **LocalizationItem**s belonging to a particular **LocalizationGroup**.

To see an example of localizing custom string constants, refer to the [How to: Localize Custom String Constants](xref:112655) help topic.