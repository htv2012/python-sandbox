<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" />

    <xsl:template match="/">
[
        <xsl:apply-templates select="Addresses/Address" />
]
    </xsl:template>
    <xsl:template match="Address">
    {
        DisplayName="<xsl:value-of select="DisplayName" />",
        DtmfAccessId="<xsl:value-of select="DtmfAccessId" />",
        SmtpAddress="<xsl:value-of select="SmtpAddress" />",
        Type="<xsl:value-of select="Type" />"
    },
    </xsl:template>
</xsl:stylesheet>

