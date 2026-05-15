In this example, XAF invokes the custom window with the embedded XAF [](xref:DevExpress.ExpressApp.ListView) when an Action `Execute` event occurs. Create a new [](xref:DevExpress.ExpressApp.ViewController) descendant and add a new [](xref:DevExpress.ExpressApp.Actions.SimpleAction) in its constructor. In the Action's `Execute` event handler, create a new instance of a custom `NonXAFForm` which is a form object. The [](xref:DevExpress.XtraLayout.LayoutControl) control correctly places custom controls on the layout. The XAF `ListView` control is created using the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) method and its controls are generated using the `CreateControls` method. Set the controls as layout items and invoke the window using the `Form.ShowDialog` method.

# [LinkViewController.cs](#tab/tabid-csharpLinkViewController-cs)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.XtraLayout;
using System.Windows.Forms;
// ...
public partial class LinkViewController : ViewController {
    public LinkViewController() {
        SimpleAction showWindowAction = new SimpleAction(this, "Show Window", PredefinedCategory.View);
        showWindowAction.ImageName = "ModelEditor_Views";
        showWindowAction.Execute += showWindowAction_Execute;
    }
    void showWindowAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        NonXAFForm form = new NonXAFForm();
        form.Text = "Form with the XAF ListView";

        LayoutControl layoutControl = new LayoutControl();
        layoutControl.Dock = System.Windows.Forms.DockStyle.Fill;
        form.Controls.Add(layoutControl);

        LayoutControlItem item1 = layoutControl.Root.AddItem();
        TextBox textBox1 = new TextBox();
        item1.Text = "Company";
        item1.Control = textBox1;

        DevExpress.ExpressApp.View listView = Application.CreateListView(typeof(Person), true);
        listView.CreateControls();
        LayoutControlItem item2 = layoutControl.Root.AddItem();
        item2.Text = "Persons";
        item2.Control = (Control)listView.Control;

        form.ShowDialog();
        listView.Dispose();
        form.Dispose();
    }
}
```

# [LinkViewController.vb](#tab/tabid-vbLinkViewController-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.XtraLayout
Imports System.Windows.Forms
' ...
Partial Public Class LinkViewController
    Inherits ViewController

    Public Sub New()
        Dim showWindowAction As New SimpleAction(Me, "Show Window", PredefinedCategory.View)
        showWindowAction.ImageName = "ModelEditor_Views"
        AddHandler showWindowAction.Execute, AddressOf showWindowAction_Execute
    End Sub
    Private Sub showWindowAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim form As New NonXAFForm()
        form.Text = "Form with the XAF ListView"

        Dim layoutControl As New LayoutControl()
        layoutControl.Dock = System.Windows.Forms.DockStyle.Fill
        form.Controls.Add(layoutControl)

        Dim item1 As LayoutControlItem = layoutControl.Root.AddItem()
        Dim textBox1 As New TextBox()
        item1.Text = "Company"
        item1.Control = textBox1

        Dim listView As DevExpress.ExpressApp.View = Application.CreateListView(GetType(Person), True)
        listView.CreateControls()
        Dim item2 As LayoutControlItem = layoutControl.Root.AddItem()
        item2.Text = "Persons"
        item2.Control = DirectCast(listView.Control, Control)

        form.ShowDialog()
        listView.Dispose()
        form.Dispose()
    End Sub
End Class
```

***
