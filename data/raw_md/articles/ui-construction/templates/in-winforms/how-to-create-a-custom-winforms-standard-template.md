---
uid: "113706"
seealso:
- linkId: "112618"
- linkId: "112696"
- linkId: "114495"
title: 'How to: Create a Custom WinForms Standard Template'
owner: Ekaterina Kiseleva
---
# How to: Create a Custom WinForms Standard Template

XAF Windows Forms applications implement either the [Standard](xref:5361) or [Ribbon](xref:2500) User Interface.

To change the user interface type, specify the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property of the Application Model's **Options** node. For instructions on how to customize a Windows Forms template for the [Ribbon User Interface](xref:2500), see the following topic: [](xref:112618).

[!include[Win_Design_Package_For_NET6+](~/templates/windesignpackagefornet6.md)]

This example demonstrates how to do the following:
* Create a custom Windows Forms template for the [Standard User Interface](xref:5361).
* Implement a new menu.
* Place a custom Action in the new menu.

## Customize a Detail Form Template

1. In the **Solution Explorer**, right-click the **YourApplicationName.Win** project and choose **Add** | **New Item…** In the invoked dialog, select **DevExpress <:xx.x:> Template Kit**, specify the item name, and click **Add** to open the [Template Kit](xref:405447). Select the **XAF WinForms Templates** | **Detail Form Template** item and click **ADD ITEM**.

   ![Template Kit, DevExpress](~/images/template-kit/template-kit-add-win-detail-form-template.png)

2. In the invoked **Detail Form Designer**, click the **[Add]** button in the Main Menu bar and choose **Menu (BarSubItem)**.

   ![Add a Bar Menu, DevExpress](~/images/winformstemplate_04117619.png)

   > [!TIP]
   > You can create a complex hierarchy of sub-menus with nested [bar sub-items](xref:DevExpress.XtraBars.BarSubItem).

3. In the Main Menu bar, focus the newly added **barSubItem1** and click the smart tag in the top right corner. In the displayed property window, set the **Caption** property to `My Actions`.

   ![Bar Menu Properties, DevExpress](~/images/standard-template-barmenu-properties-devexpress.png)
	
4. Click the **My Actions** item and click **[Add]** in the displayed menu. Choose **Inplace Link Container (BarLinkContainerExItem)** in the invoked pop-up menu.

   ![Add a Bar Link Container, DevExpress](~/images/winformstemplate_05117620.png)

5. Focus the newly added Link Container. In the **Properties** window, set the **Caption** property to `My Actions`.
	
	![Bar Link Container Properties, DevExpress](~/images/standard-template-barlinkcontainer-properties.png)
	
	> [!TIP]
	> You can also add a Link Container to the status bar. In the Status Bar Menu of the **Detail Form Designer**, click **[Add]** and select **Inplace Link Container (BarLinkContainerExItem)**.

6. Create an Action Container from the Link Container. In the bottom pane of the **Detail Form Designer**, focus the **barManager** control and click the smart tag in the top right corner. In the displayed menu, click **Run Designer**.

	![Run XAF BarManager Designer, DevExpress](~/images/winformstemplate_06117621.png)

7. In the invoked **XAF BarManager Designer** (an XAF-specific extension of the [Bar Manager Designer](xref:5353)), choose the **XAF Action Controls** | **Action Containers** item in the navigation pane and drag the **My Actions** item from the **Bar Container Controls** list to the **Action Containers** list.
	
	![Create an Action Container, DevExpress](~/images/winformstemplate_07117622.png)
	
	> [!TIP]
	> To create an Action Container from a Link Container in the status bar, drag the corresponding item from the **Bar Container Controls** list to **Action Containers**.

8. If your Action is created in code, pass the name of the Action Container to the Action's constructor as displayed in the following code snippet:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class MyViewController : ViewController {
	    public MyViewController() {
	        SimpleAction myAction = new SimpleAction(this, "MyAction", "My Actions");
	        myAction.ImageName = "Action_SimpleAction";
	    }
	}
	```
	***

	Alternatively, you can do the following:
	* Specify the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property in code.
	* Customize the **ActionDesign** | **ActionToContainerMapping** node in the [Model Editor](xref:112582). For more information about this technique, refer to the following topic: [](xref:402145).
	
9. Go to the **YourApplicationName.Win** project and open the _Program.cs_ file. Handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event to replace the default template with your custom template.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[STAThread]
	static void Main() {
	    // ...
	    winApplication.CreateCustomTemplate += delegate(object sender, CreateCustomTemplateEventArgs e) {
	        if (e.Context == TemplateContext.View) e.Template = new DetailForm1();
	    };
	    // ...
	}
	```
	***

	If your application implements both the Ribbon and the Standard User Interfaces, you need to check the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property value in the @DevExpress.ExpressApp.XafApplication.CreateCustomTemplate event handler before you specify your custom template.

	When you access the [Application Model](xref:112580), ensure that it is not set to `null`. For details, refer to the following breaking change description: [WinApplication.Setup method runs in a separate thread](https://supportcenter.devexpress.com/ticket/details/bc4941/winforms-the-winapplication-setup-method-runs-in-a-separate-thread).

		
	# [C#](#tab/tabid-csharp)

	```csharp
	winApplication.CreateCustomTemplate += delegate(object sender, CreateCustomTemplateEventArgs e) {
		if (e.Application.Model != null){
			if (((IModelOptionsWin)winApplication.Model.Options).FormStyle == RibbonFormStyle.Standard) {
				// ...
			}
		}
	};
	```
	***

	The following image illustrates the result.

	![Windows Forms Application with Customized Standard Template, DevExpress](~/images/winformstemplate_08117623.png)

> [!TIP]
> [!include[LocalizeCustomTemplate](~/templates/localizecustomtemplate111278.md)]

## Customize Multiple Templates

This example is based on a default XAF application created with the [Template Kit](xref:405447). That application implements the [Tabbed View](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) in which every invoked View opens in a new tab and all Actions are located in the main window. In this case, XAF merges the Detail and Main Form templates, and it is this merge operation that determines positions for all Main Menu bar elements.

Merging is a complex process. There are times when merging may position custom menus at the end of the Main Menu bar instead of where you specified in the **Detail Form Designer**. To avoid this behavior, create a custom Light Style Main Form template with custom menus identical to those you added to the custom Detail Form template.

If your application implements the [Multiple](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy) or [Single](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy) Window SDI View, its menus can be located in the main window and the invoked windows. In such cases, you may need to customize the Light Style Main Form template instead of the Detail Form template, or you may need to customize both templates.

The following code sample shows how to handle the `CreateCustomTemplate` event when you need to customize both templates:
	
# [C#](#tab/tabid-csharp)

```csharp
winApplication.CreateCustomTemplate += delegate(object sender, CreateCustomTemplateEventArgs e) {
	if (e.Context == TemplateContext.ApplicationWindow) {
	    e.Template = new MainForm1();
	}
	else if (e.Context == TemplateContext.View) {
	    e.Template = new DetailForm1();
	}
};
```
***