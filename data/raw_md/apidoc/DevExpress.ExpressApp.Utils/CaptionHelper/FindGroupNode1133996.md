---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.FindGroupNode(DevExpress.ExpressApp.Model.IModelApplication,System.String)
name: FindGroupNode(IModelApplication, String)
type: Method
summary: Provides access to the **LocalizationGroup** node corresponding to a specific group path.
syntax:
  content: public static IModelLocalizationGroup FindGroupNode(IModelApplication model, string groupPath)
  parameters:
  - id: model
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object representing the [Application Model](xref:112580)'s root node.
  - id: groupPath
    type: System.String
    description: A string representing the group path to the required **LocalizationGroup** node.
  return:
    type: DevExpress.ExpressApp.Model.IModelLocalizationGroup
    description: An [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) object representing the **LocalizationGroup** node corresponding to the specified group path.
seealso:
- linkId: "112595"
---
If the specified node does not exist, the **FindGroupNode** method returns `null`.

Each child **LocalizationGroup** node of the **Localization** node has a group path associated with it. This path is represented by a sequence of parent localization group names separated by a double backslash. Suppose, for example, that the **Localization** node has the **Messages** localization group, which in turn has the **Custom** child localization group. In this instance, the group path for the **Custom** group is "Messages\\Custom".

To see an example of localizing custom string constants, refer to the [How to: Localize Custom String Constants](xref:112655) help topic.