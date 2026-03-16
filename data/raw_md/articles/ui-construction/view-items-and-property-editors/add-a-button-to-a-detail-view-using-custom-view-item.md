---
uid: "113653"
seealso:
- linkId: "112816"
- linkId: "113652"
- linkId: "405483"
- linkId: "402189"
- linkId: "403258"
- linkId: "404701"

title: 'How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Fully Custom ViewItem)'
owner: Ekaterina Kiseleva
---
# How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Fully Custom ViewItem)

This article describes how to add a custom control to a Detail View. If you want to display standard [XAF Actions](xref:112622) in a Detail View, use the technique described in the following topic: [](xref:112816). 

A custom View Item should be a [](xref:DevExpress.ExpressApp.Editors.ViewItem) descendant. You can also inherit it from any of the built-in View Items that XAF supplies. For more information about View Items, refer to the following topic: [View Items](xref:112612)

## Implementation Considerations

This is an advanced customization method that requires coding. Use it when you want to add an existing or custom control to the client area of a Detail View or Dashboard View. This approach allows you to obtain data from the current View object if necessary. Your control can be unbound or can load data from external sources.

If you want to bind a control to a business class property and add that control to both List View and Detail View, then consider the [custom Property Editor approach](xref:113097#custom-property-editors).

This approach does not impose any restrictions on UI Control and XAF View interaction. You can implement custom logic in a `ViewController` or a custom UI control. [](xref:DevExpress.ExpressApp.Editors.ViewItem) descendants may implement their own inner logic.

## Create an ASP.NET Core Blazor-Specific View Item

[!example[How to: Use a Custom View Item to Add a Button to a Detail View (ASP.NET Core Blazor)](https://github.com/DevExpress-Examples/xaf-custom-view-item-blazor)]

1. Add a [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/) (_Button.razor_ in this example) to the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_). In this component, configure the @DevExpress.Blazor.DxButton component.
   
    >[!NOTE]
    > The component name and its file name should be the same. For more information on Razor component naming conventions, refer to the following section: [ASP.NET Core Razor Components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/#component-name-class-name-and-namespace).
   
    # [MySolution.Blazor.Server\Editors\Button.razor](#tab/tabid-razor)
    [!codesnippet-razor[dx-examples](xaf-custom-view-item-blazor/CS/EFCore/CustomViewItem/CustomViewItem.Blazor.Server/Editors/ButtonViewItem/Button.razor?line=1-11)]
    ```razor
    @namespace CustomViewItem.Blazor.Server.Editors.ButtonViewItem
    
    <DxButton Text=@Text Click=@Click />
    
    @code {
        [Parameter]
        public string Text { get; set; }
        [Parameter]
        public EventCallback<MouseEventArgs> Click { get; set; }
    }
    
    ```
    ***

2. Ensure that the component's [Build Action](https://learn.microsoft.com/en-us/visualstudio/ide/build-actions) property is set to `Content`.

3. Create a [ComponentModelBase](xref:404767) descendant and name it _ButtonModel_. In this class, add properties and methods that describe your component.
   
    # [MySolution.Blazor.Server\Editors\ButtonModel.cs](#tab/tabid-cs)
    [!codesnippet-cs[dx-examples](xaf-custom-view-item-blazor/CS/EFCore/CustomViewItem/CustomViewItem.Blazor.Server/Editors/ButtonViewItem/ButtonModel.cs?line=1-18)]
    ```cs
    using DevExpress.ExpressApp.Blazor.Components.Models;
    using Microsoft.AspNetCore.Components;
    using Microsoft.AspNetCore.Components.Web;
    
    namespace CustomViewItem.Blazor.Server.Editors.ButtonViewItem;
    
    public class ButtonModel : ComponentModelBase {
        public string Text {
            get => GetPropertyValue<string>();
            set => SetPropertyValue(value);
        }
        public EventCallback<MouseEventArgs> Click {
            get => GetPropertyValue<EventCallback<MouseEventArgs>>();
            set => SetPropertyValue(value);
        }
    
        public override Type ComponentType => typeof(Button);
    }
    ```
    ***

4. Add the **ButtonDetailViewItemBlazor** View Item to the [ASP.NET Core Blazor application project](xref:118045) (_MySolution.Blazor.Server_). 
   
    * Decorate this View Item with [](xref:DevExpress.ExpressApp.Editors.ViewItemAttribute) to make this View Item appear in the Application Model's **ViewItems** node.
    * Override the `CreateControlCore` method to configure and return new instance of `ButtonModel`. You can create the subscription to `Click` event right there using [EventCallback.Factory](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.eventcallbackfactory) methods.
    * Implement the logic in the `ComponentModel_Click` event handler (in this example, the `DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage` is called).
   
    # [MySolution.Blazor.Server\Editors\ButtonDetailViewItemBlazor.cs](#tab/tabid-csharp1)
    [!codesnippet-cs[dx-examples](xaf-custom-view-item-blazor/CS/EFCore/CustomViewItem/CustomViewItem.Blazor.Server/Editors/ButtonViewItem/ButtonDetailViewItemBlazor.cs?line=1-43)]
    ```cs
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor;
    using DevExpress.ExpressApp.Blazor.Components;
    using DevExpress.ExpressApp.Blazor.Components.Models;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Model;
    using Microsoft.AspNetCore.Components;
    using Microsoft.AspNetCore.Components.Web;
    
    namespace CustomViewItem.Blazor.Server.Editors.ButtonViewItem;
    
    public interface IModelButtonDetailViewItemBlazor : IModelViewItem;
    
    [ViewItem(typeof(IModelButtonDetailViewItemBlazor))]
    public class ButtonDetailViewItemBlazor(IModelViewItem model, Type objectType) : 
        ViewItem(objectType, model.Id), 
        IComponentContentHolder, 
        IComplexViewItem
    {
        public ButtonModel ComponentModel => componentModel;
        
        private ButtonModel componentModel;
        private XafApplication application;
    
        RenderFragment IComponentContentHolder.ComponentContent =>
            ComponentModelObserver.Create(componentModel, componentModel.GetComponentContent());
        void IComplexViewItem.Setup(IObjectSpace objectSpace, XafApplication application) {
            this.application = application;
        }
    
        protected override object CreateControlCore() {
            componentModel = new ButtonModel
            {
                Text = "Click me!",
                Click = EventCallback.Factory.Create<MouseEventArgs>(this, ComponentModel_Click),
            };
            return componentModel;
        }
        private void ComponentModel_Click() {
            application.ShowViewStrategy.ShowMessage("Action is executed!");
        }
    }
    
    ```
    ***

## Create a WinForms-Specific View Item

[!example[XAF - Add a Custom Button to a Form (WinForms)](https://github.com/DevExpress-Examples/xaf-win-add-custom-button-to-form-using-custom-view-item)]

1. Add the **ButtonDetailViewItemWin** View Item to the [WinForms application project](xref:118045) (_MySolution.Win_). Decorate this View Item with [](xref:DevExpress.ExpressApp.Editors.ViewItemAttribute) to make this View Item appear in the [Application Model](xref:112579)'s  **ViewItems** node.

    # [MySolution.Win\ButtonDetailViewItemWin.cs](#tab/tabid-csharp)

    ```csharp
    using System;
    using System.Windows.Forms;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Model;
    using DevExpress.ExpressApp;

    namespace MySolution.Win {
        public interface IModelButtonDetailViewItemWin : IModelViewItem { }

        [ViewItemAttribute(typeof(IModelButtonDetailViewItemWin))]
        public class ButtonDetailViewItemWin : ViewItem {
            public ButtonDetailViewItemWin(IModelViewItem model, Type objectType)
                : base(objectType, model.Id) {
            }
            protected override object CreateControlCore() {
                Button button = new Button();
                button.Text = "Click me!";
                button.Click += button_Click;
                return button;
            }
            void button_Click(object sender, EventArgs e) {
                throw new UserFriendlyException("Action is executed!");
            }
        }
    }    
    ```
    ***

2. Add the new View Item to the Detail View. Open the [Model Editor](xref:113326) and navigate to the **Views** | **MySolution.Module.BusinessObjects** | **\<Class\>** | **\<Class\>_DetailView** | **Items** node. Right-click the node and select **ButtonDetailViewItemWin** from the **Add** context menu options.
3. Navigate to the **Views** |  **MySolution.Module.BusinessObjects** | **\<Class\>** | **\<Class\>_DetailView** | **Layout** node. Right-click the layout area and select the **Customize Layout** option from the context menu. Drag the new View Item from the **Customization** window to the layout area.
