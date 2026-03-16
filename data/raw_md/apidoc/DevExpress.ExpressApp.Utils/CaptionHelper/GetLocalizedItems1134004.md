---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedItems(System.String)
name: GetLocalizedItems(String)
type: Method
summary: Returns the names and values of all the localization items for a particular **LocalizationGroup**.
syntax:
  content: public static Dictionary<string, string> GetLocalizedItems(string groupPath)
  parameters:
  - id: groupPath
    type: System.String
    description: A string representing the group path to the required **LocalizationGroup**.
  return:
    type: System.Collections.Generic.Dictionary{System.String,System.String}
    description: A **Dictionary\<String, String>** of localization item name/localization item value pairs.
seealso:
- linkId: "112595"
---
The [Application Model](xref:112580) has the **Localization** node, which allows [localization](xref:112595) of various constants. The **Localization** node is used to localize custom strings used in an **XAF** application. The node contains **LocalizationGroup** child nodes. Each **LocalizationGroup** child node contains a set of **LocalizationItem** child nodes. The **GetLocalizedItems** method allows you to retrieve the values of **LocalizationItem**s belonging to a particular **LocalizationGroup**.

Each child **LocalizationGroup** node of the **Localization** node has a group path associated with it. This path is represented by a sequence of parent localization group names separated by a double backslash. Suppose, for example, that the **Localization** node has the **Messages** localization group, which in turn has the **Custom** child localization group. In this instance, the group path for the **Custom** group is "Messages\\Custom".

To see an example of localizing custom string constants, refer to the [How to: Localize Custom String Constants](xref:112655) help topic.