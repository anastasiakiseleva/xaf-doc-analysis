---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelRootNavigationItemsBlazor.ShowNavigationOnStart
name: ShowNavigationOnStart
type: Property
summary: Specifies the initial visibility of the navigation panel in an XAF Blazor application.
syntax:
  content: |-
    [DefaultValue(true)]
    bool ShowNavigationOnStart { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to initially display the navigation panel; `false` to initially collapse the navigation panel.'
seealso: []
---
An XAF application displays the navigation panel on the left side of the window. Users can click the hamburger button to change panel visibility. 

![Application with visible navigation panel](~/images/xaf-blazor-navigation-visibility.png)

Set the `ShowNavigationOnStart` property to `false` to initially collapse the navigation when the application starts.

![Set ShowNavigationOnStart in model editor](~/images/xaf-blazor-navigation-model-editor.png)

![Application with collapsed navigation panel](~/images/xaf-blazor-navigation-collapsed.png)

The `ShowNavigationOnStart` property has no effect when the page width is less than 576 pixels. The navigation panel is initially collapsed in this case. 

![Application with navigation panel on small screen](~/images/xaf-blazor-navigation-mobile.png)