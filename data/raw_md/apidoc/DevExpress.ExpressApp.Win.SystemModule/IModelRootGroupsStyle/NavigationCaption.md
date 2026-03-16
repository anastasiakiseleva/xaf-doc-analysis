---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelRootGroupsStyle.NavigationCaption
name: NavigationCaption
type: Property
summary: Specifies the [navigation control](xref:113198)'s caption when [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) is set to **TreeList** in WinForms applications with enabled [Light Style](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle).
syntax:
  content: |-
    [DefaultValue("Navigation")]
    [ModelBrowsable(typeof(TreeListNavigationCaptionVisibilityCalculator))]
    string NavigationCaption { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the navigation control's caption.
seealso: []
---
Model Editor displays this property only when the [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property is set to **TreeList**. 

Navigate to the **NavigationItem** node and set the **NavigationCaption** property to "Navigation caption". The following image shows the result:

![NavigationCaption](~/images/NavigationCaption.png)