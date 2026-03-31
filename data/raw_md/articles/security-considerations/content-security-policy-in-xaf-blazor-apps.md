---
uid: "404448"
title: Content Security Policy (CSP) in XAF Blazor Apps
---
# Content Security Policy (CSP) in XAF Blazor Apps

[Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) (CSP) is a built-in browser
mechanism that helps you protect your web application against certain types of attacks,
such as [Cross-Site Scripting](https://learn.microsoft.com/en-us/aspnet/core/security/cross-site-scripting) (XSS),
clickjacking, and data injection. CSP is supported in most modern browsers, including Chrome, Edge, Firefox, Opera, Safari, and mobile browsers.

For additional information on how to use the Content Security Policy with an ASP.NET Core Blazor application, refer to the following Microsoft help topic:
[Enforce a Content Security Policy for ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/content-security-policy).

For general information about CSP support in DevExpress Blazor components, refer to the following topic:
[Blazor - Content Security Policy](xref:403487).

To enable CSP protection, specify a `Content-Security-Policy` header or use the `<meta>` tag and explicitly define authorized functionality with [CSP directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy). You can list allowed scripts, styles, and external domains that store required resources. Apply the following directives in the `<head>` section of the _Pages/_Host.cshtml_ file:

```CSHTML
<head>
    <!--...-->
    <meta http-equiv="Content-Security-Policy"
        content="base-uri 'self';
        default-src 'self';
        img-src data: https:;
        object-src 'none';
        script-src 'self';
        style-src 'self';
        upgrade-insecure-requests;">
    <!--...-->
</head>
```

For additional information on each directive, refer to the "Directives" section of the following topic: [Content-Security-Policy (CSP) header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy).

> [!IMPORTANT]
> To safeguard your application, always validate inline CSS styles defined in application code. Do not include user input in inline styles unless it is properly escaped/validated. Such inline styles may expose data and introduce security-related risks.

## Office Module

If you use the [Office Module](xref:400003), the [DxRichEdit](xref:DevExpress.Blazor.RichEdit.DxRichEdit) component will not work with the default CSP settings.
You will have to allow inline styles in this case.

```cshtml
<!--...-->
    style-src 'self' 'unsafe-inline';
<!--...-->
```

## Reports Module

If you use the [Reports Module](xref:113591), list the following directives in the `<head>` section of the _Pages/_Host.cshtml_ file. These directives allow print operations.

```CSHTML{11-12}
<head>
    <!--...-->
    <meta http-equiv="Content-Security-Policy"
        content="base-uri 'self';
        default-src 'self';
        img-src data: https:;
        object-src 'none';
        script-src 'self';
        style-src 'self';
        worker-src 'self' blob:;
        frame-src 'self' blob:;
        upgrade-insecure-requests;">
    <!--...-->
</head>
```

## Dashboards Module

If you use the [Dashboards Module](xref:117449), you should either allow inline styles or use a nonce-based CSP for the `style-src` directive.


## Additional Limitations and Considerations

You can find more complete information on limitations and security considerations in the following help topics:

* [Blazor - Content Security Policy](xref:403487).
* [Reports - Content Security Policy](xref:404555).
* [Dashboards - Content Security Policy](xref:404190).