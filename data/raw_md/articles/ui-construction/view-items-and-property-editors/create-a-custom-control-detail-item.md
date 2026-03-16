---
uid: "113652"
seealso:
- linkId: "112816"
- linkId: "113653"
- linkId: "404701"
title: 'How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Built-in ControlViewItem)'
---
# How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Built-in ControlViewItem)

This article describes how to add a custom control to a **Detail View**. Use this approach when you need to place a custom control near a particular editor in a **Detail View** and the [Action Container View Item](xref:112816) method is not suitable (this method does not allow data access from the current view object).

## Implementation Considerations

This suggested implementation requires minimal coding. Use it when you want to add an existing or custom control to the client area of a Detail View or Dashboard View. This approach allows you to obtain data from the current View object if necessary. Your control can be unbound or can load data from external sources.

If you want to bind a control to a business class property and need to add the control to both List View and Detail View, then consider the [custom Property Editor approach](xref:113097#custom-property-editors).

This approach also does not imply complex user interactions between the UI control and an XAF View. You can implement a custom `ViewController` if you require custom logic. A custom UI control may implement advanced user interaction.

## ASP.NET Core Blazor

1. Navigate to the ASP.NET Core Blazor [application project](xref:118045) (_SolutionName.Blazor.Server_) and create an **Editors** folder.
2. In the **Editors** folder, create a [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/) and name it _ButtonComponent.razor_.

    > [!NOTE]
    > The component name and its file name should be the same. For more information on Razor component naming conventions, refer to the following section: [ASP.NET Core Razor Components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/#component-name-class-name-and-namespace).

3. In this component, configure the @DevExpress.Blazor.DxButton component:
   * Use the cascading parameter to access the current `BlazorControlViewItem`.
   * Implement the `ClickFromUI()` method to specify a message that should appear when a user clicks the button in the UI.

    # [CS\SolutionName.Blazor.Server\Editors\ButtonComponent.razor](#tab/tabid-razor)
    ```Razor
    @using DevExpress.Blazor
    @using DevExpress.ExpressApp
    @using DevExpress.ExpressApp.Blazor.Editors

    <DxButton Text="Click me!" Click=@ClickFromUI />

    @code {
        [CascadingParameter]
        public BlazorControlViewItem ViewItem { get; set; }
        private void ClickFromUI() {
            ViewItem.Application.ShowViewStrategy.ShowMessage("Action is executed!");
        }
    }
    ```
    ***

4. Right-click the Razor file to access its properties and make sure that the `Build Action` property is set to `Content`.

5. Add the component to a Detail View. Open the [Model Editor](xref:113326) and navigate to the **Views** | **SolutionName.Module.BusinessObjects** | **\<Class\>** | **\<Class\>_DetailView** | **Items** node. Right-click the node and select **Add** | **ControlDetailItem** from the context menu options.
6. Specify the Razor component's full type name in the **ControlTypeName** property: **SolutionName.Blazor.Server.Editors.ButtonComponent**.

    ![XAF Add A Control Detail Item in the Model Editor, DevExpress](~/images/xaf-model-editor-add-controldetailitem-devexpress.png)

7. Navigate to the **Views** | **SolutionName.Module.BusinessObjects** |**\<Class\>** | **\<Class\>_DetailView** | **Layout** node. Right-click the layout area and select the **Customize Layout** option from the context menu. Drag the new View Item from the **Customization: \<Class\>** window to the layout area.

8. Run the application and navigate to the required Detail View. Click the **Click Me!** button. A toast notification should appear:

    ![|XAF ASP.NET Core Blazor Button View Item in a Detail View, DevExpress](~/images/xaf-blazor-add-button-to-detail-view-devexpress-result.png)

## Windows Forms

1. Navigate to the _MySolution.Win_ project and open the _Model.xafml_ file. In the [Model Editor](xref:112582), navigate to the **Views** | **MySolution.Module.BusinessObjects** | **\<Class\>** | **\<Class\>_DetailView** | **Items** node. Right-click the node and select **ControlDetailItem** from the **Add** context menu.

2. Set the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property of the newly created node to `System.Windows.Forms.Button`. Set the `Id` property to `MyButton` and [IModelViewItem.Caption](xref:DevExpress.ExpressApp.Model.IModelViewItem.Caption) to `My Button`.

    ![XAF Windows Forms, Add ControlDetailItem in Model Editor, DevExpress](~/images/ht_add_button2_1117523.png)

3. Navigate to the **Views** | **MySolution.Module.BusinessObjects** |**\<Class\>** | **\<Class\>_DetailView** | **Layout** node. Right-click the layout area and select the **Customize Layout** option from the context menu. Drag the new View Item from the **Customization: \<Class\>** window to the layout area.

    ![XAF Windows Forms, Customize Detail View Layout, DevExpress](~/images/ht_add_button2_2117524.png)

    For more information about layout customization, refer to the following topic: [](xref:112817).

4. Run the application and navigate to the Detail View. The new Action should be available in the UI:

    ![XAF Windows Forms, Button in Detail View, DevExpress](~/images/xaf-winforms-controlviewitem-button-devexpress.png)

5. To handle the Action's `Click` event, add a new Controller to the _MySolution.Win_ project and replace the automatically generated code:

    # [MySolution.Win\Controllers\ControlViewItemControllerWin.cs](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Win.Controllers;
    public class ControlViewItemControllerWin : ObjectViewController<DetailView, Employee> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl(this, (viewItem) => {
                if (viewItem.Control is Button button) {
                    button.Text = "Click me!";
                    button.Click += ButtonClickHandlingWinController_Click;
                }
            });
        }
        void ButtonClickHandlingWinController_Click(object sender, EventArgs e) {
            MessageBox.Show("Action from custom View Item was executed!");
        }
    }
    ```
    ***

6. Run the application. Navigate to the required Detail View and click the button. The following message should appear:

    ![|XAF Windows Forms, Information Message on Button Click, DevExpress](~/images/xaf-winforms-controlviewitem-result-devexpress.png)
