---
uid: "113151"
seealso: []
title: Customize the Logon Window Appearance And Behavior
owner: Vera Ulitina
---
# Customize the Logon Window Appearance And Behavior

A logon window contains a [Detail View](xref:112611) like most other [XAF Windows](xref:112608). For instance, the **Password** and **User Name** fields represent View Items.

![Tutorial_SS_Lesson1_1](~/images/tutorial_ss_lesson1_1115528.png)

You can customize the logon window using one of the following techniques:

* **Using the** [Model Editor](xref:112582)
	
	The **Views** | **AuthenticationStandardLogonParameters_DetailView** node defines the Detail View used in the logon window, by default. Here, you can customize the Detail View's settings, change the list of displayed View Items, change items' layout, localize the captions, etc. See the following topics for more information:
	
	* [How to: Include an Action to a Detail View Layout](xref:112816)
	* [View Items Layout Customization](xref:112817)
	* [Localization Basics](xref:112595)

	> [!NOTE]
	> * In an ASP.NET Core Blazor application, modify either **AuthenticationStandardLogonParameters_Blazor_DetailView** or **NoPasswordLogonParameters_DetailView** (depending on whether the password authentication is enabled).
	> * In a Windows Forms application, modify either **AuthenticationStandardLogonParameters_Win_DetailView** or **NoPasswordLogonParameters_Win_DetailView** (depending on whether the password authentication is enabled).

* **Creating a Controller**
	
	Create a Controller and [activate it for the logon form](xref:113475#activate-a-controller-for-the-logon-form).
	
* **Adding Editors**
	
	To add an editor to the Detail View and use the typed information during user authentication, use a custom LogonParameters type and modified **AuthenticationStandard** class. To learn how to do this, refer to the following topics:
	
	* [](xref:404264)
	* [Security System Overview](xref:113366)
	* [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize)
	* [User Authentication using a Logon Window in Windows Forms Applications](xref:113117)
