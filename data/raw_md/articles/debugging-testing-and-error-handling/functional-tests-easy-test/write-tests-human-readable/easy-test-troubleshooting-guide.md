---
uid: "113293"
seealso: []
title: EasyTest Troubleshooting Guide
---
# EasyTest Troubleshooting Guide

This topic provides a list of common issues that may be encountered while using EasyTest, along with ways to resolve them. Follow the recommendations below if you face a problem with EasyTest.

> [!NOTE]
> If you face an issue that is not listed here, please do the following. Review the information in the [TestExecutor's](xref:113210) XML output logs, and in the [log file](xref:112575) of the application being tested. Information in these files, logged at the moment when the error occurs, may help you understand the cause of the issue. Additionally, ensure that the [EasyTest configuration file](xref:113209) is located in the same directory as the test script you are attempting to run and contains the correct settings (application names, paths, port numbers). If this does not help, please [submit a support ticket](https://supportcenter.devexpress.com/ticket/create), specify how you run the test (from Visual Studio or using TestExecutor) and attach your log files, a screenshot of the error and your project (if possible).

## A System.ArgumentOutOfRangeException occurs when you try to run an EasyTest script

Problem Description:

When running an EasyTest script, the following error message is displayed.

_Caught the 'System.ArgumentOutOfRangeException' exception. Exception text: 'Index was out of range. Must be non-negative and less than the size of the collection.'
Parameter name: index', stack trace: '   at System.ThrowHelper.ThrowArgumentOutOfRangeException()_

Solution:

You must have administrative privileges to run EasyTest scripts. So if a script fails to run, make sure that you run Visual Studio using the "Run as administrator" option. For additional information, refer to the [How to use User Account Control (UAC)](https://support.microsoft.com/en-us/windows/what-does-it-mean-if-windows-isn-t-supported-08f3b92d-7539-671e-1452-2e71cdad18b5) document.

## EasyTest cannot log-on to an application that uses a complex custom splash screen

Problem Description:

When trying to run an EasyTest script for an application that uses a complex custom [splash screen](xref:112680), the application stays at the LogOn window indefinitely.

Solution:

If you use a custom splash form, note that EasyTest implies the splash screen form has a "Splash" substring in its name. EasyTest skips such a form at application startup. So, the issue occurs when a name of a class that implements the custom splash form contains no "Splash" substring. There are two options for fixing it.

* Rename the class that implements your custom splash form, so its name contains "Splash" (e.g., MyCustomSplashForm).
* Handle the **CheckIsFormAcceptable** event of the **DevExpress.ExpressApp.EasyTest.WinAdapter.ProcessFormsEnumerator** class, and set the **Cancel** parameter to **False** when the splash form is being processed.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	DevExpress.ExpressApp.EasyTest.WinAdapter.ProcessFormsEnumerator.CheckIsFormAcceptable += 
	    delegate(object sender, System.ComponentModel.CancelEventArgs e) {
	    Form form = sender as Form;
	    e.Cancel = e.Cancel || 
	    (form != null && form.Name == MySolution.Win.MyCustomForm.FormName);
	};
	```

	***


## A "No connection could be made because the target machine actively refused it 127.0.0.1:4100" error occurs

Problem Description:

When trying to run an EasyTest script for a Windows  Forms application, the following error occurs.

_No connection could be made, because the target machine actively refused it 127.0.0.1:4100_

Solution:

* Ensure that the **Main** method in the _Program.cs_ file contains the following code.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	static void Main() {
	#if EASYTEST
	    DevExpress.ExpressApp.Win.EasyTest.EasyTestRemotingRegistration.Register();
	#endif
	    // ...
	}
	```

	***
* Check the Windows Forms application definition in the [EasyTest configuration file](xref:113209). The **FileName** attribute must point to an executable that is built with an **EasyTest** configuration (not **Debug** or **Release**). The **CommunicationPort** value must be 4100, as this is the default port listened to by EasyTest.
	
	# [XML](#tab/tabid-xml)
	
	```XML
	<Application
	    Name = "MySolutionWin"
	    FileName="D:\Projects\MySolution\MySolution.Win\Bin\EasyTest\MySolution.Win.exe"
	    AdapterAssemblyName="DevExpress.ExpressApp.EasyTest.WinAdapter.v, 
	    Version=.0, Culture=neutral, PublicKeyToken=b88d1754d700e49a"
	    CommunicationPort="4100"/>
	```
	
	***
	
	If you want to use another port, specify the **EasyTestCommunicationPort**  key value in the application configuration file (_App.config_).
	
	# [XML](#tab/tabid-xml)
	
	```XML
	<appSettings>
	    <!-- ... -->
	    <add key="EasyTestCommunicationPort" value="44100"/>
	    <!-- ... -->
	</appSettings>
	```
	
	***
* Check that connections to the specified port are not blocked by your firewall and no other software uses that port.

***

If this document does not contain sufficient information on how to resolve your issue, feel free to contact Developer Express support engineers at the [Support Center](https://supportcenter.devexpress.com).
