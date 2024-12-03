SYSTEM_PROMPT = """You are an expert digital marketing copywriter specializing in educational course promotion. Your task is to generate compelling ad copy variations for a digital marketing course."""
    
USER_PROMPT = """
<ProjectInstructions>
    <Objective>
        Please create 12 unique Google Ad concepts, one for each of the following strategies. Incorporate the provided keywords naturally into the ads where they fit best while maintaining the style and strategy of each ad type. Ensure that the output is formatted as **valid XML**, using the structure below:
    </Objective>
    
    <InputFields>
        <BusinessDetails>{business_details}</BusinessDetails>
        <Keywords>{keywords}</Keywords>
    </InputFields>
    
    <AdConcepts>
        <AdConcept>
            <Name>The Niche Expert</Name>
            <Example>We Do Swing Sets, Nothing Else</Example>
            <Style>Highlight specialization in a specific area. Use a conversational tone that inspires confidence. Show you understand the customer's perspective.</Style>
        </AdConcept>
        <AdConcept>
            <Name>The Differentiator</Name>
            <Example>The Customer Service Platform – Based on Customers Not Tickets</Example>
            <Style>Use a "this, not that" phrase to distinguish your offering from competitors. Focus on what makes your approach unique.</Style>
        </AdConcept>
        <AdConcept>
            <Name>The Standout Feature</Name>
            <Example>Best Customer Service Software – AI to Deduct User Sentiments</Example>
            <Style>Highlight a very specific, unique feature that sets you apart. Make it intriguing enough to drive clicks, even if you don't fully explain it.</Style>
        </AdConcept> 
        <AdConcept> 
            <Name>The Benefit Banker</Name>
            <Example>Focus, Energy, Clarity – Hours of Focus, Zero Crash</Example>
            <Style>Focus entirely on benefits, not features. Highlight outcomes the customer will experience. You don't even need to mention your product category.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Target Filter</Name>
            <Example>Small Business Loans – Requires $100K + Annual Revenue</Example>
            <Style>Include a pre-qualification element to filter leads. Be specific about who your product/service is for, even if it seems restrictive.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Alliterative Artist</Name>
            <Example>Fiverr Freelance Services – Hire Pros for Your Projects</Example>
            <Style>Use alliteration or other word play in the headline. Create a rhythm that makes the ad pleasant to read and memorable.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Scorekeeper</Name>
            <Example>#1 Organic Online Market, 30% Off Top Brands, 1M+ Members</Example>
            <Style>Use numbers and statistics as trust signals. Replace adjectives with specific data points to boost credibility.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Conversationalist</Name>
            <Example>Top Copywriting Services – No Blogspam, No Keyword Fluff</Example>
            <Style>Use casual, industry-specific language that resonates with your audience. Speak to them in their own words.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Speed Demon</Name>
            <Example>Ask a Lawyer: Fraud – Lawyer Will Answer in Minutes</Example>
            <Style>Emphasize quick service or fast results. Use concise language that's easy to skim, reinforcing the idea of speed.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Pain Point Prodder</Name>
            <Example>No follow through? – Are they dropping the ball?</Example>
            <Style>Use the Pain-Agitate-Solution (P-A-S) formula. Identify a pain point, agitate it, then offer your solution. Use emotional triggers.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Subtle Competitor</Name>
            <Example>Don't Hire Those Guys, Really – We Can Beat Their Prices</Example>
            <Style>Indirectly compare yourself to competitors. Be bold but not aggressive. This works well when you're not the top ad.</Style>
        </AdConcept>   
        <AdConcept>
            <Name>The Key Message Reinforcer</Name>
            <Example>Don't Overpay For Rackets – Avoid Paying Full Price</Example>
            <Style>Repeat a key message for emphasis. Use slightly different wording to reinforce the main point without being repetitive.</Style>
        </AdConcept> 
    </AdConcepts>
    
    <OutputRequirements>
        <Headlines>
            <Count>3</Count>
            <MaxLength>30</MaxLength>
            <Description>Unique headline options that can be used together in any combination without being redundant</Description>
        </Headlines>
        <Description>
            <MaxLength>90</MaxLength>
            <ComplimentaryText>Compliments the headline</ComplimentaryText>
        </Description>
        <Explanation>
            <Content>Brief explanation of how it applies the strategy and incorporates keywords</Content>
        </Explanation>
    </OutputRequirements>
    
    <Guidelines>
        <CharacterLimits>Adhere to Google Ads character limits</CharacterLimits>
        <Relevance>Ensure ads are relevant to my business and audience</Relevance>
        <CallToAction>Use compelling calls-to-action</CallToAction>
        <KeywordUsage>Incorporate provided keywords naturally</KeywordUsage>
    </Guidelines>
    
    <FormattingInstructions>
        <MainHeadings>H1</MainHeadings>
        <Subheadings>H2</Subheadings>
        <ThirdLevelHeadings>H3</ThirdLevelHeadings>
        <ParagraphText>Regular text for paragraphs or explanations</ParagraphText>
    </FormattingInstructions>


    <GoogleAdConcepts>
    <Concept>
        <StrategyName>The Niche Expert</StrategyName>
        <Headlines>
            <Headline>Headline 1</Headline>
            <Headline>Headline 2</Headline>
            <Headline>Headline 3</Headline>
        </Headlines>
        <Description>Complimentary description text</Description>
        <Explanation>Explanation of the strategy and keyword incorporation</Explanation>
    </Concept>
        <!-- Repeat for each strategy -->
    </GoogleAdConcepts>
</ProjectInstructions>

"""