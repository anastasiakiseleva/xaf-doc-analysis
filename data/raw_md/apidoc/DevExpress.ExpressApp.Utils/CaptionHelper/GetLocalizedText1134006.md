---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedText(System.String,System.String,System.String)
name: GetLocalizedText(String, String, String)
type: Method
summary: Returns the value of a specified **LocalizationItem**.
syntax:
  content: public static string GetLocalizedText(string groupPath, string itemName, string defaultText)
  parameters:
  - id: groupPath
    type: System.String
    description: A string representing the group path to the **LocalizationGroup** containing the specified localization item.
  - id: itemName
    type: System.String
    description: A string holding the [IModelLocalizationItemBase.Name](xref:DevExpress.ExpressApp.Model.IModelLocalizationItemBase.Name) of the required **LocalizationItem** node.
  - id: defaultText
    type: System.String
    description: A string that will be returned by the **GetLocalizedText** method, if the specified localization item is not found.
  return:
    type: System.String
    description: The [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) of the specified localization item.
seealso:
- linkId: "112595"
---
The [Application Model](xref:112580) has the **Localization** node, which allows [localization](xref:112595) of various constants. The **Localization** node is used to localize custom strings used in an **XAF** application. The node contains **LocalizationGroup** child nodes. Each **LocalizationGroup** child node contains a set of **LocalizationItem** child nodes. The **GetLocalizedText** method allows you to retrieve the value of particular **LocalizationItem**.

Each child **LocalizationGroup** node of the **Localization** node has a group path associated with it. This path is represented by a sequence of parent localization group names separated by a double backslash. Suppose, for example, that the **Localization** node has the **Messages** localization group, which in turn has the **Custom** child localization group. In this instance, the group path for the **Custom** group is "Messages\\Custom".

To see an example of localizing custom string constants, refer to the [How to: Localize Custom String Constants](xref:112655) help topic.