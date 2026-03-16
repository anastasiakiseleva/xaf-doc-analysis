---
uid: "112820"
seealso: []
title: "How to: Replace a List View's Default Action"
owner: Ekaterina Kiseleva
---
# How to: Replace a List View's Default Action

[List Views](xref:112611) can be accompanied by [Actions](xref:112622) that represent features specific to these List Views. In addition to these Actions, every List View has an invisible default Simple Action. In Windows Forms applications, this Action is executed when pressing the ENTER key or double-clicking a selected object. In ASP.NET Core Blazor applications, this Action is executed when an object is clicked. This Action is specified by the [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController)'s [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) property. You can replace this Action with a custom Simple Action. This topic demonstrates how to do this.

## Set a Custom Action as Default

Assume you have the following `AddressBookRecord` persistent class.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions,ImageName("BO_Contact")]
public class AddressBookRecord : BaseObject {
    public virtual string Name { get; set; }
    public virtual string Email { get; set; }
    public virtual string PhoneNumber { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions, ImageName("BO_Contact")]
public class AddressBookRecord : BaseObject {
    public AddressBookRecord(Session session) : base(session) { }
    private string name;
    public string Name {
        get { return name; }
        set { SetPropertyValue(nameof(Name), ref name, value); }
    }
    private string email;
    public string Email {
        get { return email; }
        set { SetPropertyValue(nameof(Email), ref email, value); }
    }
    private string phoneNumber;
    public string PhoneNumber {
        get { return phoneNumber; }
        set { SetPropertyValue(nameof(PhoneNumber), ref phoneNumber, value); }
    }
}
```
***

Let us consider the `WriteMailController` [View Controller](xref:112621) that provides the **WriteMail** Action for `AddressBookRecord` objects. This Action invokes the program that is associated with the **MailTo** protocol on an end-user's computer.

> [!NOTE]
> ASP.NET Core Blazor applications do not allow you to start system processes, but you can use this approach to execute another Action.

# [C#](#tab/tabid-csharp)

```csharp
using System.Diagnostics;
// ...
public class WriteMailController : ViewController {
    private SimpleAction writeMailAction;
    public WriteMailController() {
        TargetObjectType = typeof(AddressBookRecord);
        writeMailAction = new SimpleAction(this, "WriteMail", PredefinedCategory.Edit);
        writeMailAction.ToolTip = "Write e-mail to the selected address book record";
        writeMailAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        writeMailAction.ImageName = "BO_Contact";
        writeMailAction.Execute += writeMailAction_Execute;
    }
    void writeMailAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        AddressBookRecord record = (AddressBookRecord)e.CurrentObject;
        string startInfo = String.Format(
            "mailto:{0}?body=Hello, {1}!%0A%0A", record.Email, record.Name);
        Process.Start(startInfo);
    }
}
```
***

By default, the Action specified by the `ProcessCurrentObjectAction` property of the `ListViewProcessCurrentObjectController` invokes a Detail View with the clicked object (the **ListViewShowObject** Action is specified by default). However, the `ListViewProcessCurrentObjectController` exposes the [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event, which you can handle to replace the default Action. The code below demonstrates how to handle this event in `WriteMailController` to execute a **WriteMail** Action instead of **ListViewShowObject**. Subscribe to the `CustomProcessSelectedItem` event in the overridden `OnActivated` method. In the event handler, execute the **WriteMail** Action by invoking the [SimpleAction.DoExecute](xref:DevExpress.ExpressApp.Actions.SimpleAction.DoExecute) method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
// ...
public class WriteMailController : ViewController {
    // ...
    private ListViewProcessCurrentObjectController processCurrentObjectController;
    protected override void OnActivated() {
        base.OnActivated();
        processCurrentObjectController =
            Frame.GetController<ListViewProcessCurrentObjectController>();
        if (processCurrentObjectController != null) {
            processCurrentObjectController.CustomProcessSelectedItem +=
                processCurrentObjectController_CustomProcessSelectedItem;
        }
    }
    private void processCurrentObjectController_CustomProcessSelectedItem(
        object sender, CustomProcessListViewSelectedItemEventArgs e) {
        e.Handled = true;
        writeMailAction.DoExecute();
    }
    protected override void OnDeactivated() {
        if (processCurrentObjectController != null) {
            processCurrentObjectController.CustomProcessSelectedItem -= 
                processCurrentObjectController_CustomProcessSelectedItem;
        }
        base.OnDeactivated();
    }
}
```
***

The following image illustrates that the **WriteMail** action is executed when clicking a record in the `AddressBookRecord` objects' List View.

![ReplaceDefaultActionWin](~/images/replacedefaultactionwin116905.png)

You may notice that now there is no option to invoke a Detail View to edit a record. You can add to following Controller to fix this.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
// ...
public class EditAddressBookRecordController : ViewController<ListView> {
    public EditAddressBookRecordController() {
        TargetObjectType = typeof(AddressBookRecord);
        SimpleAction editAddressBookRecordAction = 
            new SimpleAction(this, "EditAddressBookRecord", PredefinedCategory.Edit);
        editAddressBookRecordAction.ImageName = "Action_Edit";
        editAddressBookRecordAction.SelectionDependencyType = 
            SelectionDependencyType.RequireSingleObject;
        editAddressBookRecordAction.Execute += editAddressBookRecordAction_Execute;
    }
    void editAddressBookRecordAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        ListViewProcessCurrentObjectController.ShowObject(
            e.CurrentObject, e.ShowViewParameters, Application, Frame, View);
    }
}
```
***

![ReplaceDefaultActionWin1](~/images/replacedefaultactionwin1116906.png)

To leave an option to replace the **WriteMail** Action in another Controller, you can expose this action via a public property.

# [C#](#tab/tabid-csharp)

```csharp
public class WriteMailController : ViewController {
    // ...
    public SimpleAction DefaultListViewAction {
        get { return writeMailAction; }
        set { writeMailAction = value; }
    }
}
```
***

Proceed to the next section of this topic to see how this property can be used.

## Replace a Custom Default Action
Consider the following `PhoneCallController` View Controller than provides the **PhoneCall** Action. This action initiates dialing `PhoneNumber` of the current `AddressBookRecord` object in `Skype`.

# [C#](#tab/tabid-csharp)

```csharp
public class PhoneCallController : ViewController {
    private SimpleAction phoneCallAction;
    public PhoneCallController() {
        TargetObjectType = typeof(AddressBookRecord);
        phoneCallAction = new SimpleAction(this, "PhoneCall", PredefinedCategory.Edit);
        phoneCallAction.ToolTip = "Call the current record via Skype";
        phoneCallAction.ImageName = "BO_Phone";
        phoneCallAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        phoneCallAction.Execute += skypeCallAction_Execute;
    }
    void skypeCallAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Process.Start("skype:" + ((AddressBookRecord)e.CurrentObject).PhoneNumber);
    }
    protected override void OnActivated() {
        base.OnActivated();
        View.CurrentObjectChanged += View_CurrentObjectChanged;
    }
    void View_CurrentObjectChanged(object sender, EventArgs e) {
        phoneCallAction.Enabled.SetItemValue("PhoneIsSpecified",
            !String.IsNullOrEmpty(((AddressBookRecord)View.CurrentObject).PhoneNumber));
    }
}
```
***

> [!NOTE]
> ASP.NET Core Blazor applications do not allow you to start system processes, but you can use this approach to execute another Action.

The List View's default Action provided by the custom `WriteMailController` Controller can be replaced with another Action, if it is exposed via a public property. To replace the **WriteMail** action with **PhoneCall**, add the following code to the `PhoneCallController` class' `OnActivated` method.

# [C#](#tab/tabid-csharp)

```csharp
protected override void OnActivated() {
    // ...
    WriteMailController writeMailController = Frame.GetController<WriteMailController>();
    if (writeMailController != null)
        writeMailController.DefaultListViewAction = phoneCallAction;
}
```
***

The following image illustrates that the **PhoneCall** action is executed when clicking a record in the `AddressBookRecord` objects' List View.

![ReplaceDefaultActionWin2](~/images/replacedefaultactionwin2116907.png)

Subscribing to the `ListViewProcessCurrentObjectController`'s `CustomProcessSelectedItem` event, as demonstrated at the beginning of this topic is not a recommended, since there is the possibility that the `PhoneCallController` Controller will be activated after `WriteMailController`, and so the **WriteMail** Action will remain default.

