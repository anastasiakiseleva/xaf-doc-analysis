---
uid: "405643"
title: 'Display and Customize the Ribbon UI in an XAF Blazor Application'
---
# Display and Customize the Ribbon UI in an XAF Blazor Application

An XAF Core Blazor application can display the standard [Toolbar UI](xref:DevExpress.Blazor.DxToolbar) or [Ribbon UI](xref:DevExpress.Blazor.DxRibbon). If you create a new application, XAF sets the UI type to `Ribbon`.

> [!ImageGallery]
> ![Ribbon UI](~/images/xaf-blazor-form-style-ribbon.png)
> ![Standard UI](~/images/xaf-blazor-form-style-standard.png)

## Display the Ribbon UI in an Existing Application

In the **Solution Explorer**, expand the _MySolution.Blazor.Server_ project and double-click the _Model.xafml_ file to open it in the [Model Editor](xref:112582). Navigate to the **Options** node and set the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle property to `Ribbon`.

![Ribbon UI Setup in Model Editor, DevExpress](~/images/xaf-blazor-form-style-option.png)

## Customize the Ribbon UI

An XAF application builds the Ribbon UI structure based on the model specified in the [Model Editor](xref:112582). You can customize the default Ribbon structure as follows:

1. In the **Solution Explorer**, expand the _MySolution.Blazor.Server_ project and double-click the _Model.xafml_ file to open it in the [Model Editor](xref:112582).
2. Navigate to the **Action Design | ActionToRibbonMapping** node. 

    Use the **ActionToRibbonMapping** node to customize default ribbon elements or add custom elements.

    * The **ActionToRibbonMapping** node contains a list of ribbon page models (<xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage>).  
    You can specify a page @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Caption, order @DevExpress.ExpressApp.Model.IModelNode.Index, and whether the page is @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Contextual. Contextual pages are displayed after standard ribbon pages and their headers are highlighted.
    * A ribbon page model contains a list of ribbon page group models (<xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPageGroup>).  
    You can specify a group @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Caption and order @DevExpress.ExpressApp.Model.IModelNode.Index.
    * A ribbon page group model contains a list of [Action Container](xref:112610) links (<xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelActionContainerToRibbonLink>).  
    Use the @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionContainerToRibbonLink.ActionContainer property to link an Action Container and the @DevExpress.ExpressApp.Model.IModelNode.Index property to order links in the group.
    * An Action Container contains a list of action links (<xref:DevExpress.ExpressApp.SystemModule.IModelActionLink>). To access these elements, navigate to the **Action Design | ActionToContainerMapping** node. See the following help topic for more information: <xref:112815>.



![Ribbon Scheme](~/images/xaf-blazor-ribbon-scheme.png)

## Access the DxRibbon Component

1. Under the _SolutionName.Blazor.Server_ project, [add a Window Controller](xref:405447#create-a-new-item) to the _Controllers_ folder.
2. Override the `OnActivated` method as demonstrated in the following code snippet:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Services;
using DevExpress.ExpressApp.Blazor.Templates.Ribbon;

public class TabsCustomizationWindowController : WindowController {
    private IImageUrlService imageUrlService;

    public TabsCustomizationWindowController() {
        TargetWindowType = WindowType.Main;
    }
    [ActivatorUtilitiesConstructor]
    public TabsCustomizationWindowController(IImageUrlService imageUrlService) : this() {
        this.imageUrlService = imageUrlService;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Window.TemplateChanged += Window_TemplateChanged;
    }
    protected override void OnDeactivated() {
        Window.TemplateChanged -= Window_TemplateChanged;
        base.OnDeactivated();
    }
    private void Window_TemplateChanged(object sender, EventArgs e) {
        if(Window.Template is ITemplateRibbonProvider ribbonProvider) {
            ribbonProvider.Ribbon.RibbonModel.DropDownMenuMaxHeight = "400px";
            foreach(var tab in ribbonProvider.Ribbon.Tabs) {
                tab.IconUrl = imageUrlService.GetImageUrl("BO_Unknown");
            }
        }
    }
}
```

You can use the @DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl event to access and customize individual Action control items in `DxRibbon`, such as `DxRibbonItemSimpleActionControl` and other `DxRibbonItemXXXControl` types.