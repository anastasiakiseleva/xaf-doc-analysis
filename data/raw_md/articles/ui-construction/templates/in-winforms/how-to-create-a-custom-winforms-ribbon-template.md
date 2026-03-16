---
uid: "112618"
seealso:
- linkId: "112696"
- linkId: "113706"
- linkId: "114495"
- linkId: "404212"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-create-information-panels
  altText: 'How to: Create Information Panels'
title: 'How to: Create a Custom WinForms Ribbon Template'
owner: Ekaterina Kiseleva
---
# How to: Create a Custom WinForms Ribbon Template

XAF Windows Forms applications implement either the [Standard User Interface](xref:5361) or the [Ribbon User Interface](xref:2500).

To change the user interface type, specify the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property of the Application Model's **Options** node. For instructions on how to customize a Windows Forms template for the [Standard User Interface](xref:5361), see the following topic: [](xref:113706).

[!include[Win_Design_Package_For_NET6+](~/templates/windesignpackagefornet6.md)]

This example demonstrates how to do the following:
* Create a custom Windows Forms template for the [Ribbon User Interface](xref:2500).
* Implement a new Ribbon Page.
* Place a custom Action in the new Ribbon Page.

## Customize a Detail Form Template

1. In the **Solution Explorer**, right-click the **YourApplicationName.Win** project and choose **Add** | **New Item…**. In the invoked dialog, select **DevExpress <:xx.x:> Template Kit**, specify the item name, and click **Add** to invoke the [Template Kit](xref:405447). Select **XAF** | **XAF WinForms Templates** | **Detail Ribbon Form Template** and click **ADD ITEM**.
	
	![Template Kit, DevExpress](~/images/template-kit/template-kit-add-win-detail-ribbon-form-template.png)

2. In the invoked **Ribbon Form Designer**, focus the Ribbon Control, click the smart tag in the top right corner, and click **Run Designer**.
	
	![Run Designer option, DevExpress](~/images/ribbontemplate_04117605.png)

3. In the invoked **XAF Ribbon Control Designer**, choose the **Toolbars** item in the navigation pane and create a new [Ribbon Page Group](xref:2493). You can add it to an existing [Ribbon Page](xref:2494) or create a custom [Page Category](xref:3327), add a new Ribbon Page, and create a new Ribbon Page Group in this Page.
	
	![XAF Ribbon Control Designer, DevExpress](~/images/ribbontemplate_05117606.png)
	
	> [!NOTE]
	> **XAF Ribbon Control Designer** is an XAF-specific extension of the [Ribbon Control Designer](xref:2623). Refer to the following topic to learn how to manage ribbon items, ribbon pages, and page groups: [Toolbars Page](xref:403840).

4. Close the **XAF Ribbon Control Designer** window. In the **Ribbon Form Designer**, right-click the new Ribbon Page Group and choose **Add Inplace Link Container (BarLinkContainerExItem)**.
	
	![Add a Link Container, DevExpress](~/images/ribbontemplate_055119009.png)

	> [!TIP]
	> You can also add a Link Container to the status bar. In the Status Bar Menu of the Ribbon Form Designer, right-click **StatusMessages** and choose **Add Inplace Link Container (BarLinkContainerExItem)**.

5. Click the smart tag in the top right corner of the container item. In the displayed property window, set the **Caption** property to `My Actions`.
	
	![Link Container Properties, DevExpress](~/images/ribbontemplate_056119010.png)

6. Create an Action Container from the link container. Open the **XAF Ribbon Control Designer**, choose the **XAF Action Controls** | **Action Containers** item in the navigation pane, and drag the **My Actions** item from the **Bar Container Controls** list to the **Action Containers** list.
	
	![Action Containers List, DevExpress](~/images/ribbontemplate_06117607.png)
	
	> [!TIP]
	> To create an Action Container from a Link Container in the status bar, drag the corresponding item from the **Bar Container Controls** list to **Action Containers**.

7. Select the **My Actions** item in the **Action Containers** list and specify the **ActionCategory** property. For example, set it to `MyActionCategory`.
	
	![Action Container Category, DevExpress](~/images/ribbontemplate_07117608.png)

8. Create an Action that is triggered by the button in the Ribbon control. For step-by-step instructions, refer to the following XAF In-Depth .NET WinForms & Blazor UI Tutorial: [](xref:402157).

   If your Action is created in code, pass the name of the Action Category specified in the previous step to the Action's constructor as displayed in the following code snippet:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp{3}
	public class MyViewController : ViewController {
	    public MyViewController() {
	        SimpleAction myAction = new SimpleAction(this, "MyAction", "MyActionCategory");
	        myAction.ImageName = "Action_SimpleAction";
	    }
	}
	```
	***
	
	Alternatively, you can:
	* Specify the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property in code.
	* Customize the **ActionDesign** | **ActionToContainerMapping** node in the [Model Editor](xref:112582). For more information about this technique, refer to the following topic: [](xref:402145).

9. Go to the **YourApplicationName.Win** project and open the _Program.cs_ file. Handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event to replace the default template with your custom template.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[STAThread]
	static void Main() {
	    // ...
	    winApplication.CreateCustomTemplate += delegate(object sender, CreateCustomTemplateEventArgs e) {
	        if (e.Context == TemplateContext.View) e.Template = new DetailRibbonForm1();
	    };
	    // ...
	}
	```
	***

	If your application implements both the Ribbon User Interface and the Standard User Interface, you need to check the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property value in the @DevExpress.ExpressApp.XafApplication.CreateCustomTemplate event handler before you specify your custom template.

	When you access the [Application Model](xref:112580), ensure that it is not set to `null`. For details, refer to the following breaking change description: [WinApplication.Setup method runs in a separate thread](https://supportcenter.devexpress.com/ticket/details/bc4941/winforms-the-winapplication-setup-method-runs-in-a-separate-thread).

	# [C#](#tab/tabid-csharp)

	```csharp{5}
	[STAThread]
	static void Main() {
	    // ...
		winApplication.CreateCustomTemplate += delegate(object sender, CreateCustomTemplateEventArgs e) {
			if(e.Application.Model != null){
				if (((IModelOptionsWin)winApplication.Model.Options).FormStyle == RibbonFormStyle.Ribbon) {
					// ...
				}
			}
		};
		// ...
	}
	```
	***

	The following image illustrates the result:

	![Windows Forms Application with Customized Ribbon Template, DevExpress](~/images/ribbontemplate_08117609.png)

> [!TIP]
> [!include[LocalizeCustomTemplate](~/templates/localizecustomtemplate111278.md)]

## Customize Multiple Templates

This example is based on a default XAF application created with the [Template Kit](xref:405447). That application implements the [Tabbed View](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) in which every newly invoked View opens as a new tab and all Actions are located in the main window. In this case, XAF
merges [Detail Ribbon Form](xref:403446#detail-ribbon-form-template-detailribbonformv2) and [Light Style Main Ribbon Form](xref:403446#main-ribbon-form-template-lightstylemainribbonform) templates, and it is this merge operation that determines positions of all ribbon elements.

Merging is a complex process. There are times, when merging may position custom Page Groups at the end of the ribbon instead of where you specified in the **Ribbon Form Designer**. To avoid this behavior, create a custom Light Style Main Ribbon Form template with custom Page Groups identical to those you added to the custom Detail Ribbon Form template.

If your application implements the [Multiple](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy) or [Single](xref:DevExpress.ExpressApp.Win.ShowInSingleWindowStrategy) Windows SDI View, its Actions can then be located in the main window and in the invoked windows. In such cases, you may need to customize the Light Style Main Ribbon Form template instead of the Detail Ribbon Form template, or you may need to customize both of them at once.

The following code sample shows how to handle the `CreateCustomTemplate` event when you have to customize both templates:
	
# [C#](#tab/tabid-csharp)

```csharp
winApplication.CreateCustomTemplate += delegate (object sender, CreateCustomTemplateEventArgs e) {
	if (e.Context == TemplateContext.ApplicationWindow) {
		e.Template = new LightStyleMainRibbonForm1();
	}
	else if (e.Context == TemplateContext.View) {
		e.Template = new DetailRibbonForm1();
	}
};
```
***
