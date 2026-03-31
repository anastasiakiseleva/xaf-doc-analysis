---
uid: "112816"
seealso:
- linkId: "113652"
- linkId: "113653"
- linkId: "112803"
- linkId: "112804"
- linkId: "17574"
- linkId: "404701"
title: 'How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Built-in ActionContainerViewItem)'
---
# How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Built-in ActionContainerViewItem)

XAF allows you to place an Action in a View instead of a toolbar. 

In the image below, the "My Simple Action" button is an Action displayed in a Detail View.

![|XAF ASP.NET Core Blazor Action in a Detail View, DevExpress|](~/images/blazor-detailview-add-action-button.png)

## Implementation Considerations

This is the simplest approach that requires minimal coding. If you have an existing Controller and Action, then no code is necessary. Use this method when you want to add a simple button, a drop-down button, a pop-up menu, or an input box to the client area of a Detail View or Dashboard View.

This approach relies on the standard XAF Action and Controller events for user interaction and does not require obtaining data from the current View object.

## Step 1. Create a new Action

In the `MySolution.Module` project, add a new class to the `Controllers` folder. Replace its content with the following code:

# [CS\MainDemo.Module\Controllers](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Module.Controllers {
    public class MyViewController : ViewController {
        public MyViewController() {
            TargetViewType = ViewType.DetailView;
            TargetObjectType = typeof(Employee);

            SimpleAction mySimpleAction = new SimpleAction(this, "MySimpleAction", "MyCategory") {
                Caption = "My Simple Action",
                ConfirmationMessage = "My Simple Action Shows a Message",
            };
            mySimpleAction.Execute += MySimpleAction_Execute;
        }
        private void MySimpleAction_Execute(Object sender, SimpleActionExecuteEventArgs e) {
            // ...
        }

    }
}
```
***

Rebuild your project.

## Step 2. Place a New Action in a Detail View

1. In the _MainDemo.Module_ project, open the _Model.DesignedDiffs.xafml_ file. If the **Model Editor** is already open, restart it and navigate to the **Views** node.

2. In the **Views** node, navigate to the Detail View where you want to display the action. Invoke the context menu to add a new **ActionContainerViewItem** child node to the Detail View's items node.
	
	![XAF Model Editor Add ActionContainerViewItem, DevExpress](~/images/ht_add_button1_2117519.png)

2. Set the newly created node's `Id` property to `MyActionContainer` and the `ActionContainer` property to `MyCategory`.
	
	![XAF Model Editor Layout Customization, DevExpress](~/images/ht_add_button1_3117520.png)

3. Select the Detail View's **Layout** node. In the layout designer, right-click the empty space and invoke the layout customization dialog and drag the newly created control from the list of hidden items to the layout.
	
	![XAF Model Editor Layout Customization, DevExpress](~/images/ht_add_button1_4117521.png)

	For more information on how to customize the view layout, refer to the following topic: [View Items Layout Customization](xref:112817).

4. Run the application. The Action button is visible in the required Detail View:

   ASP.NET Core Blazor
   :   ![|XAF ASP.NET Core Blazor Action in a Detail View, DevExpress|](~/images/blazor-detailview-add-action-button.png)
   Windows Forms
   :   ![|sXAF Windows Forms Action in a Detail View, DevExpress](~/images/ht_add_button1_5117522.png)

## Step 3. Customize an Action in the Layout (Optional)

Handle the [Action.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event to customize Action controls.

The following code samples demonstrate how to:

* Render an Action button in the primary style of the current theme in an ASP.NET Core Blazor application.
* Remove paddings and adjust an Action button size to match an input text box size in a Windows Forms application.

# [(Blazor) CS\MainDemo.Blazor.Server\Controllers](#tab/tabid-blazor)
 
```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Templates.Toolbar.ActionControls;

namespace YourApplicationName.Module.Controllers {
	public class MyViewController : ObjectViewController<DetailView, MyObject> {
    	public MyViewController() {
        	var action = new SimpleAction(this, "Test", "My");
        	action.CustomizeControl += Action_CustomizeControl;
    	}
    	private void Action_CustomizeControl(object sender, CustomizeControlEventArgs e) {
        	if(e.Control is DxToolbarItemSimpleActionControl actionControl) {
            	actionControl.ToolbarItemModel.RenderStyle = ButtonRenderStyle.Primary;
        	}
    	}
	}
}
```

# [(WinForms) CS\MainDemo.Win\Controllers](#tab/tabid-win)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.XtraLayout;
using System.Windows.Forms;

namespace YourApplicationName.Module.Controllers {
	public class MyViewController : ObjectViewController<DetailView, MyObject> {
		public MyViewController() {
			var action = new SimpleAction(this, "Test", "My");
			action.CustomizeControl += Action_CustomizeControl;
		}
		private void Action_CustomizeControl(object sender, CustomizeControlEventArgs e) {
			Control control = (Control)e.Control;
			LayoutControl layoutControl = (LayoutControl)control.Parent;
			LayoutControlItem item = layoutControl.GetItemByControl(control);
			item.Padding = new DevExpress.XtraLayout.Utils.Padding(0);
			layoutControl.OptionsView.AutoSizeInLayoutControl = AutoSizeModes.UseMinSizeAndGrow;
		}
	}
}
```
***

If you define an Action in the platform-independent [module project](xref:118045), you can create a platform-specific descendant and handle the [Action.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event in the descendant's constructor.

Alternatively, create a new platform-specific [Controller](xref:112621). In the Controller's `OnActivated` method, call the [Frame.GetController](xref:DevExpress.ExpressApp.Frame.GetController``1) method to get the platform-independent Controller. Use the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property to get the Action and handle its [Action.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event.

For more information on Windows Forms layout item settings, refer to the following topic : [](xref:17574).

> [!NOTE]
> In Windows Forms applications, XAF creates a `ButtonsContainer` class (a [Layout Control](xref:3407) descendant) for each `ActionContainerViewItem` and places the `ButtonsContainer` in a Detail View layout. All Action controls are located in this class. If Action control customization does not meet your requirements, you can customize the `ButtonsContainer` class.
