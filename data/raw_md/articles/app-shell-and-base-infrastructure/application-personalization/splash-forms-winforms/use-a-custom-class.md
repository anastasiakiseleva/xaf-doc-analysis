---
uid: '400737'
title: 'Use a Custom Class to Show a Splash Form (WinForms)'
---

# Use a Custom Class to Show a Splash Form (WinForms)

This topic demonstrates how create a custom [splash form](xref:112680) and use a custom class to show this form.

1. Create a new Windows Form in your solution's [WinForms Application project](xref:118045), name the form **SplashScreenForm**, and design it to meet your requirements.

    ![Splash](~/images/splash115401.png)

    > [!Note]
    > [!include[DesignTime_WinForms_NuGet_Net5](~/templates/DesignTime_WinForms_NuGet_Net5.md)]

2. Add a new class to your [WinForms Application Project](xref:118045) and implement the @DevExpress.ExpressApp.Win.ISplash interface.
	*  Override the [ISplash.Start](xref:DevExpress.ExpressApp.Win.ISplash.Start) method. Create a **SplashScreenForm** instance and call the form's [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form.show) method.
	* In the [ISplash.Stop](xref:DevExpress.ExpressApp.Win.ISplash.Stop) method's override, hide and close the **SplashScreenForm**.
	* The [ISplash.IsStarted](xref:DevExpress.ExpressApp.Win.ISplash.IsStarted) property indicates whether the **SplashScreenForm** is shown.
	* Override [ISplash.SetDisplayText](xref:DevExpress.ExpressApp.Win.ISplash.SetDisplayText(System.String)). You can call this method to change the **SplashScreenForm**'s text.

    The code below demonstrates the **MySplash** class that implements the **ISplash** interface.

	# [C#](#tab/tabid-csharp)

	```csharp
	using DevExpress.ExpressApp.Win;
	//...
	public class MySplash : ISplash {
		static private SplashScreenForm form;
		private static bool isStarted = false;
		public void Start() {
			isStarted = true;
			form = new SplashScreenForm();
			form.Show();
			System.Windows.Forms.Application.DoEvents();
		}
		public void Stop() {
			if(form != null) {
				form.Hide();
				form.Close();
				form = null;
			}
			isStarted = false;
		}
		public void SetDisplayText(string displayText) {
		}
		public bool IsStarted {
			get { return isStarted; }
		}
	}
	```
	***


3. Access the _WinApplication.cs_ (_WinApplication.vb_) file. Set the @DevExpress.ExpressApp.Win.WinApplication.SplashScreen property to a new **MySplash** class instance.

    # [C#](#tab/tabid-csharp)
	
	```csharp
	public MySolutionWindowsFormsApplication() {
	   //...
	   SplashScreen = new MySplash();
	   // ...
	}
	```
	***


4. You can display loading progress information. To do this, implement the the [](xref:DevExpress.ExpressApp.Win.ISupportUpdateSplash) interface in the **MySplash** class and add the **UpdateInfo** method to the **SplashScreenForm** class.


	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class MySplash : ISplash, ISupportUpdateSplash {
	    // ...
	    public void UpdateSplash(string caption, string description, params object[] additionalParams) {
	        form.UpdateInfo(description);
	    }
	}
	// ...
	public partial class SplashScreenForm : Form {
	    // ...
	    internal void UpdateInfo(string info) {
	        label2.Text = info;
	    }
	}
	```
	***
	
5. Start the application to see the result.
	
    ![CustomSplashForm](~/images/customsplashform117225.png)
