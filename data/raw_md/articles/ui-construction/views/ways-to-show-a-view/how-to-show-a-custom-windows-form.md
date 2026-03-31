---
uid: "118222"
seealso:
- linkId: "112803"
- linkId: "118240"
- linkId: "118165"
title: 'How to: Show a Custom Windows Form'
---
# How to: Show a Custom Windows Form

In XAF WinForms applications, it is possible to show custom windows using standard Windows Forms approaches, such as the **Form.Show** and **Form.ShowDialog** methods. If a Form should show data from the application's database, it is possible to use XAF mechanisms for CRUD operations using the [](xref:DevExpress.ExpressApp.IObjectSpace) interface. This topic demonstrates how to initialize and show a custom Form when an XAF Action is clicked.

## Show a Custom Window
The steps below describe how to show a custom window on an [Action](xref:112622)'s **Execute** event.

* Create and design a custom Form, for example, a **NonXAFForm**.
* Create a new [](xref:DevExpress.ExpressApp.ViewController) descendant and add a new [](xref:DevExpress.ExpressApp.Actions.SimpleAction) in its constructor.
* Create a new **NonXAFForm** instance in the Action's **Execute** event handler.
* Invoke the window using the **Form.ShowDialog** method.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Actions;
	using System.Windows.Forms;
	//...
	public class ShowWindowController : ViewController {
	    public ShowWindowController() {
	        SimpleAction showWindowAction = new SimpleAction(this, "ShowWindow", 
	DevExpress.Persistent.Base.PredefinedCategory.View);
	        showWindowAction.ImageName = "ModelEditor_Views";
	        showWindowAction.Execute += 
	new SimpleActionExecuteEventHandler(showWindowAction_Execute);
	    }
	    void showWindowAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
	        NonXAFForm form = new NonXAFForm();
	        //...
	        form.ShowDialog();
	    }
	}
	```
	***

![CustomWindowWithoutXAFData](~/images/customwindowwithoutxafdata127583.png)

## Show a Custom Window with XAF Data
In this example, a custom window with a control that displays XAF data is invoked when an [Action](xref:112622)'s **Execute** event occurs. The **DataGridView** control is used here for demonstration purposes. Follow the steps below to implement this behavior:

* Create a new [](xref:DevExpress.ExpressApp.ViewController) descendant and add a new [](xref:DevExpress.ExpressApp.Actions.SimpleAction) in its constructor.
* In the Action's **Execute** event handler, create a new form instance.
* Create a new [](xref:DevExpress.ExpressApp.IObjectSpace) instance using the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method.
* Get a **Contact** type objects collection using the [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) method and set it as the **DataGridView** control's data source.
* Place the **DataGridView** control on the Form and invoke this Form using the **Form.ShowDialog** method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using System.Collections;
using System.Windows.Forms;
//...
public class ShowWindowController : ViewController {
    public ShowWindowController() {
        SimpleAction showWindowAction = new SimpleAction(this, "ShowWindow", 
DevExpress.Persistent.Base.PredefinedCategory.View);
        showWindowAction.ImageName = "ModelEditor_Views";
        showWindowAction.Execute += 
new SimpleActionExecuteEventHandler(showWindowAction_Execute);
    }
    void showWindowAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Form form = new Form();
        form.Text = "Form with XAF Data";
        IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Contact));
        IList contactsCollection = objectSpace.CreateCollection(typeof(Contact));
        DataGridView dataGridView = new DataGridView();
        dataGridView.DataSource = contactsCollection;
        dataGridView.Dock = DockStyle.Fill;
        form.Controls.Add(dataGridView);
        form.ShowDialog();
    }
}
```
***

![CustomWindowWithXAFData](~/images/customwindowwithxafdata127506.png)

You can display XAF data in a control of an existing form by adding the form's constructor with the **IObjectSpace** parameter. In this constructor, specify the control's **DataSource** property using the [IObjectSpace.GetObjects](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*) method. The code snippet below shows an example of this constructor.

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp;
using DevExpress.XtraEditors;
//...
public partial class NonXAFForm : XtraForm {
    //...
    private IObjectSpace objectSpace;
    public NonXAFForm(IObjectSpace objectSpace) : base() {
        InitializeComponent();
        this.objectSpace = objectSpace;
        dataGridView1.DataSource = objectSpace.GetObjects(typeof(Contact));
        //...
    }
}
```
***