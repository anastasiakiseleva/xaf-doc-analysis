---
uid: "118549"
seealso: []
title: Text Notifications
---
# Text Notifications

In XAF applications, you can display a message box with a detailed notification text using the [ShowViewStrategyBase.ShowMessage](xref:DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage*) method.

## DevExpress Components and Widgets Used to Show Notifications

XAF uses the DevExpress WinForms and ASP.NET Core Blazor components and widgets to show the notifications for WinForms and ASP.NET Core Blazor applications.

### ASP.NET Core Blazor Notifications

Blazor applications support the following notification API:

- [MessageOptions.CancelDelegate](xref:DevExpress.ExpressApp.MessageOptions.CancelDelegate)
- [MessageOptions.Duration](xref:DevExpress.ExpressApp.MessageOptions.Duration)
- [MessageOptions.Message](xref:DevExpress.ExpressApp.MessageOptions.Message)
- [MessageOptions.OkDelegate](xref:DevExpress.ExpressApp.MessageOptions.OkDelegate)
- [MessageOptions.Type](xref:DevExpress.ExpressApp.MessageOptions.Type)
- [WebMessageOptions.OkButtonText](xref:DevExpress.ExpressApp.WebMessageOptions.OkButtonText)
- [WebMessageOptions.CssClass](xref:DevExpress.ExpressApp.WebMessageOptions.CssClass)
- [WebMessageOptions.ShowCloseButton](xref:DevExpress.ExpressApp.WebMessageOptions.ShowCloseButton)

### Windows Forms Notifications

You can choose one of the three available notification types listed in the [](xref:DevExpress.ExpressApp.WinMessageType) enumeration for a WinForms application:

Alert
:   The notification is displayed using the [Alert Window](xref:5395).
Toast
:   The notification window is displayed using the [Toast Notification Manager](xref:17020). Used only in Windows 8 or later.
Flyout
:   The notification window is displayed using the [Flyout Dialog](xref:114568).

## Using Text Notifications

To display a "Success" message when a user clicks the platform-independent **Mark Completed** Action, use the @DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage(DevExpress.ExpressApp.MessageOptions) method. The [](xref:DevExpress.ExpressApp.MessageOptions) class contains both the platform-agnostic and platform-specific settings of a text notification.

# [C#](#tab/tabid-csharp)

```csharp{29-35,41}
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Module.Controllers {
    public class DemoTaskController : ViewController {
        public DemoTaskController() {
            TargetObjectType = typeof(DemoTask);
            TargetViewType = ViewType.Any;
            SimpleAction markCompletedAction = new SimpleAction(
                this, "MarkCompleted",
                DevExpress.Persistent.Base.PredefinedCategory.RecordEdit) {
                TargetObjectsCriteria =
                    (CriteriaOperator.Parse("Status != ?", MySolution.Module.BusinessObjects.TaskStatus.Completed)).ToString(),
                ConfirmationMessage =
                            "Are you sure you want to mark the selected task(s) as 'Completed'?",
                ImageName = "State_Task_Completed"
            };
            markCompletedAction.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
            markCompletedAction.Execute += (s, e) => {
                foreach (DemoTask task in e.SelectedObjects) {
                    task.DueDate = DateTime.Now;
                    task.Status = MySolution.Module.BusinessObjects.TaskStatus.Completed;
                    View.ObjectSpace.SetModified(task);
                }
                View.ObjectSpace.CommitChanges();
                View.ObjectSpace.Refresh();
                MessageOptions options = new MessageOptions();
                options.Duration = 2000;
                options.Message = string.Format("{0} task(s) have been successfully updated!", e.SelectedObjects.Count);
                options.Type = InformationType.Success;
                options.Web.Position = InformationPosition.Right;
                options.Win.Caption = "Success";
                options.Win.Type = WinMessageType.Toast;
                options.OkDelegate = () => {
                    IObjectSpace os = Application.CreateObjectSpace(typeof(DemoTask));
                    DetailView newTaskDetailView = Application.CreateDetailView(os, os.CreateObject<DemoTask>());
                    Application.ShowViewStrategy.ShowViewInPopupWindow(newTaskDetailView);
                };
                Application.ShowViewStrategy.ShowMessage(options);
            };
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Public Class ProjectTaskController
    Inherits ViewController
    '…
    Private options As New MessageOptions()
    options.Duration = 2000
    options.Message = String.Format("{0} task(s) have been successfully updated!", e.SelectedObjects.Count)
    options.Type = InformationType.Success
    options.Web.Position = InformationPosition.Right
    options.Win.Caption = "Success"
    options.Win.Type = WinMessageType.Toast
    options.OkDelegate = Sub()
        Dim os As IObjectSpace = Application.CreateObjectSpace(GetType(ProjectTask))
        Dim newTaskDetailView As DetailView = Application.CreateDetailView(os, os.CreateObject(Of ProjectTask)())
        Application.ShowViewStrategy.ShowViewInPopupWindow(newTaskDetailView)
    End Sub
    Application.ShowViewStrategy.ShowMessage(options)
End Class
```

***

ASP.NET Core Blazor  
:   ![|A Text Notification in XAF ASP.NET Core Blazor Application, DevExpress|](~/images/showmessage_blazor.png)
Windows Forms 
:   ![|A Text Notification in XAF Windows Forms Application, DevExpress|](~/images/showmessage_win127649.png)

> [!IMPORTANT]
> * In Windows Forms applications, the Toast Notifications Manager requires [an application shortcut pinned to the Windows 10 start screen](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/hh802768(v=vs.85)) to display Toast notifications correctly. Once you do this, you need to customize the [](xref:DevExpress.XtraBars.ToastNotifications.ToastNotificationsManager) instance as described in the following topic: [Toast Notification Manager](xref:17020). Use the @DevExpress.ExpressApp.Win.WinShowViewStrategyBase.CustomizeToastNotificationsManager event to access the instance.

## Notifications Customization

* Use the [WinMessageOptions.ImageOptions](xref:DevExpress.ExpressApp.WinMessageOptions.ImageOptions) property to change the default image of the WinForms notifications the [Toast](xref:17020) or [Alert](xref:5395) control displays:

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.Drawing;
	using DevExpress.ExpressApp;
	using DevExpress.Utils;
	using DevExpress.Utils.Svg;
	//...
	MessageOptions options = new MessageOptions();
	ImageOptions imageOptions = new ImageOptions();
	//imageOptions.Image = Image.FromFile(@"D:\Images\success.png");
	// or
	imageOptions.SvgImage = SvgImage.FromFile(@"D:\Images\success.svg");
	imageOptions.SvgImageSize = new Size(50, 50);
	options.Win.ImageOptions = imageOptions;
	Application.ShowViewStrategy.ShowMessage(options);
	```
	
	# [VB.NET](#tab/tabid-vb)
	
	```vb
	Imports System.Drawing
	Imports DevExpress.ExpressApp.Win
	'...
	    CType(Application.ShowViewStrategy, WinShowViewStrategyBase).CustomGetImage += _
	ShowMessagesController_CustomGetImage
	    '...
	    Private Sub ShowMessagesController_CustomGetImage(ByVal sender As Object, _
	ByVal e As CustomGetImageEventArgs)
	        e.Image = New Bitmap(32, 32)
	        '...
	    End Sub
	```
	
	***

    Alternatively, you can use the `WinShowViewStrategyBase` class's `CustomGetImage` event as shown below:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.Drawing;
	using DevExpress.ExpressApp.Win;
	//...
	    ((WinShowViewStrategyBase)Application.ShowViewStrategy).CustomGetImage += 
	    ShowMessagesController_CustomGetImage;
	    //...
	    void ShowMessagesController_CustomGetImage(object sender, CustomGetImageEventArgs e) {
	        e.Image = new Bitmap(32, 32); 
	        //...
	    }
	```
	
	# [VB.NET](#tab/tabid-vb)
	
	```vb
	Imports System.Drawing
	Imports DevExpress.ExpressApp.Win
	'...
	    CType(Application.ShowViewStrategy, WinShowViewStrategyBase).CustomGetFlyoutBackColor += _
	    ShowMessagesController_CustomGetFlyoutBackColor
	    '...
	    Private Sub ShowMessagesController_CustomGetFlyoutBackColor(ByVal sender As Object, _
	    ByVal e As CustomGetFlyoutBackColorEventArgs)
	        If e.InformationType = InformationType.Error Then
	            e.BackColor = Color.Red
	        End If
	    End Sub
	```
	
	***
* Use the `WinShowViewStrategyBase` class's `CustomGetFlyoutBackColor` event to change the [Flyout Dialog](xref:114568)'s color:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.Drawing;
	using DevExpress.ExpressApp.Win;
	//...
	    ((WinShowViewStrategyBase)Application.ShowViewStrategy).CustomGetFlyoutBackColor += 
	    ShowMessagesController_CustomGetFlyoutBackColor;
	    //...
	    void ShowMessagesController_CustomGetFlyoutBackColor(object sender, CustomGetFlyoutBackColorEventArgs e) { 
	        if(e.InformationType == InformationType.Error) {
	            e.BackColor = Color.Red;
	        } 
	    }
	```
	
	# [VB.NET](#tab/tabid-vb)
	
	```vb
	Imports System.Drawing
	Imports DevExpress.ExpressApp.Win
	'...
	    CType(Application.ShowViewStrategy, WinShowViewStrategyBase).CustomGetFlyoutBackColor += _
	    ShowMessagesController_CustomGetFlyoutBackColor
	    '...
	    Private Sub ShowMessagesController_CustomGetFlyoutBackColor(ByVal sender As Object, _
	    ByVal e As CustomGetFlyoutBackColorEventArgs)
	        If e.InformationType = InformationType.Error Then
	            e.BackColor = Color.Red
	        End If
	    End Sub
	```
	
	***

* Use the `WinShowViewStrategyBase` class's `CustomizeAlertControl` event to customize the [Alert](xref:5395) control:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Utils;
	using DevExpress.ExpressApp.Win;
	using DevExpress.XtraBars.Alerter;
	//...
	    ((WinShowViewStrategyBase)Application.ShowViewStrategy).CustomizeAlertControl += 
	ShowMessagesController_CustomizeAlertControl;
	    //...
	    void ShowMessagesController_CustomizeAlertControl(object sender, CustomizeAlertControlEventArgs e) {
	        AlertButton button = new AlertButton(ImageLoader.Instance.GetImageInfo("BO_Attention").Image);
	        button.Name = "buttonAlert";
	        e.AlertControl.Buttons.Add(button);
	        //...
	    }
	```
	
	# [VB.NET](#tab/tabid-vb)
	
	```vb
	Imports DevExpress.ExpressApp.Utils
	Imports DevExpress.ExpressApp.Win
	Imports DevExpress.XtraBars.Alerter
	'...
	    AddHandler CType(Application.ShowViewStrategy, WinShowViewStrategyBase).CustomizeAlertControl, _
	AddressOf ShowMessagesController_CustomizeAlertControl
	    '...
	    Private Sub void ShowMessagesController_CustomizeAlertControl(Object sender, _
	CustomizeAlertControlEventArgs e)
	        Dim button As New AlertButton(ImageLoader.Instance.GetImageInfo("BO_Attention").Image)
	        button.Name = "buttonAlert"
	        e.AlertControl.Buttons.Add(button)
	        '...
	    End Sub
	```
	
	***

* Use the `WinShowViewStrategyBase` class's `CustomizeToastNotificationsManager` to access the [Toast Notification Manager](xref:17020) instance:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Win;
	//...
	    ((WinShowViewStrategyBase)Application.ShowViewStrategy).CustomizeToastNotificationsManager +=
	ShowMessagesController_CustomizeToastNotificationsManager;
	    //...
	    void ShowMessagesController_CustomizeToastNotificationsManager(object sender, 
	CustomizeToastNotificationsManagerEventArgs e) {
	        e.ToastNotificationsManager.UserCancelled += ToastNotificationsManager_UserCancelled;
	    }
	    void ToastNotificationsManager_UserCancelled(object sender, 
	DevExpress.XtraBars.ToastNotifications.ToastNotificationEventArgs e) {
	        //...
	    }
	```
	
	# [VB.NET](#tab/tabid-vb)
	
	```vb
	Imports DevExpress.ExpressApp.Win
	'...
	    AddHandler CType(Application.ShowViewStrategy, WinShowViewStrategyBase).CustomizeToastNotificationsManager, _
	AddressOf ShowMessagesController_CustomizeToastNotificationsManager
	    '...
	    Private Sub void ShowMessagesController_CustomizeToastNotificationsManager(Object sender, _
	CustomizeToastNotificationsManagerEventArgs e)
	        AddHandler e.ToastNotificationsManager.UserCancelled, AddressOf _
	ToastNotificationsManager_UserCancelled
	    Ens Sub
	    Private Sub void ToastNotificationsManager_UserCancelled(Object sender, _
	DevExpress.XtraBars.ToastNotifications.ToastNotificationEventArgs e)
	        '...
	    End Sub
	```
	
	***

## Notification Button Caption Localization

You can localize the notification button captions using the Model Editor. Navigate to the **Localization** | **DialogButtons** node, choose the **OK** or **Cancel** node and set a particular string to the **Value** property. Note that this setting also applies to other dialog buttons.

![Notification_Localization](~/images/notification_localization128228.png)
