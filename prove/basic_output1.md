[ Skip to content ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluate-a-simple-llm-application)
**Ragas Office Hours** - If you need help setting up Evals for your AI application, sign up for our Office Hours [here](https://cal.com/team/ragas/office-hours). 
[ ![logo](https://docs.ragas.io/en/latest/_static/imgs/ragas-logo.png) ](https://docs.ragas.io/en/latest/ "Ragas")
Ragas 
Evaluate your first LLM App 
Initializing search 
[ explodinggradients/ragas 
  * v0.3.1
  * 10.3k
  * 1k

](https://github.com/explodinggradients/ragas "Go to repository")
  * [ ](https://docs.ragas.io/en/latest/)
  * [ 🚀 Get Started ](https://docs.ragas.io/en/latest/getstarted/)
  * [ 📚 Core Concepts ](https://docs.ragas.io/en/latest/concepts/)
  * [ 🧪 Experimental ](https://docs.ragas.io/en/latest/experimental/)
  * [ 🛠️ How-to Guides ](https://docs.ragas.io/en/latest/howtos/)
  * [ 📖 References ](https://docs.ragas.io/en/latest/references/)
  * [ ❤️ Community ](https://docs.ragas.io/en/latest/community/)


[ ![logo](https://docs.ragas.io/en/latest/_static/imgs/ragas-logo.png) ](https://docs.ragas.io/en/latest/ "Ragas") Ragas 
[ explodinggradients/ragas 
  * v0.3.1
  * 10.3k
  * 1k

](https://github.com/explodinggradients/ragas "Go to repository")
  * [ ](https://docs.ragas.io/en/latest/)
  * [ 🚀 Get Started  ](https://docs.ragas.io/en/latest/getstarted/)
    * [ Installation  ](https://docs.ragas.io/en/latest/getstarted/install/)
    * Evaluate your first LLM App  [ Evaluate your first LLM App  ](https://docs.ragas.io/en/latest/getstarted/evals/)
      * [ Evaluation  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluation)
        * [ Evaluating using a Non-LLM Metric  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-using-a-non-llm-metric)
        * [ Evaluating using a LLM based Metric  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-using-a-llm-based-metric)
        * [ Evaluating on a Dataset  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-on-a-dataset)
        * [ Want help in improving your AI application using evals?  ](https://docs.ragas.io/en/latest/getstarted/evals/#want-help-in-improving-your-ai-application-using-evals)
      * [ Up Next  ](https://docs.ragas.io/en/latest/getstarted/evals/#up-next)
    * [ Evaluate a simple RAG  ](https://docs.ragas.io/en/latest/getstarted/rag_eval/)
    * [ Generate Synthetic Testset for RAG  ](https://docs.ragas.io/en/latest/getstarted/rag_testset_generation/)
  * [ 📚 Core Concepts  ](https://docs.ragas.io/en/latest/concepts/)
    * [ Components  ](https://docs.ragas.io/en/latest/concepts/components/)
      * General 
        * [ Prompt  ](https://docs.ragas.io/en/latest/concepts/components/prompt/)
      * Evaluation 
        * [ Evaluation Sample  ](https://docs.ragas.io/en/latest/concepts/components/eval_sample/)
        * [ Evaluation Dataset  ](https://docs.ragas.io/en/latest/concepts/components/eval_dataset/)
    * [ Metrics  ](https://docs.ragas.io/en/latest/concepts/metrics/)
      * [ Overview  ](https://docs.ragas.io/en/latest/concepts/metrics/overview/)
      * [ Available Metrics  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/)
        * Retrieval Augmented Generation 
          * [ Context Precision  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/context_precision/)
          * [ Context Recall  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/context_recall/)
          * [ Context Entities Recall  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/context_entities_recall/)
          * [ Noise Sensitivity  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/noise_sensitivity/)
          * [ Response Relevancy  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/answer_relevance/)
          * [ Faithfulness  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/)
        * Nvidia Metrics 
          * [ Answer Accuracy  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/nvidia_metrics/#answer-accuracy)
          * [ Context Relevance  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/nvidia_metrics/#context-relevance)
          * [ Response Groundedness  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/nvidia_metrics/#response-groundedness)
        * Agents or Tool Use Cases 
          * [ Agentic or Tool use  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/agents/)
          * [ Topic Adherence  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/agents/#topic-adherence)
          * [ Tool Call Accuracy  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/agents/#tool-call-accuracy)
          * [ Agent Goal Accuracy  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/agents/#agent-goal-accuracy)
        * Natural Language Comparison 
          * [ Factual Correctness  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/factual_correctness/)
          * [ Semantic Similarity  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/semantic_similarity/)
          * Traditional non LLM metrics 
            * [ Traditional NLP Metrics  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/)
            * [ Non LLM String Similarity  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#non-llm-string-similarity)
            * [ BLEU Score  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#bleu-score)
            * [ ROUGE Score  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#rouge-score)
            * [ String Presence  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#string-presence)
            * [ Exact Match  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#exact-match)
        * SQL 
          * [ SQL  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/sql/)
          * [ Execution based Datacompy Score  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/sql/#execution-based-metrics)
          * [ SQL Query Equivalence  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/sql/#sql-query-semantic-equivalence)
        * General Purpose 
          * [ General Purpose Metrics  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/general_purpose/)
          * [ Aspect Critic  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/general_purpose/#aspect-critic)
          * [ Simple Criteria Scoring  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/general_purpose/#simple-criteria-scoring)
          * [ Rubrics Based Scoring  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/general_purpose/#rubrics-based-criteria-scoring)
          * [ Instance Specific Rubrics Scoring  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/general_purpose/#instance-specific-rubrics-criteria-scoring)
        * Other Tasks 
          * [ Summarization  ](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/summarization_score/)
    * [ Test Data Generation  ](https://docs.ragas.io/en/latest/concepts/test_data_generation/)
      * RAG 
        * [ Testset Generation for RAG  ](https://docs.ragas.io/en/latest/concepts/test_data_generation/rag/)
        * [ KG Building  ](https://docs.ragas.io/en/latest/concepts/test_data_generation/rag/#knowledge-graph-creation)
        * [ Scenario Generation  ](https://docs.ragas.io/en/latest/concepts/test_data_generation/rag/#scenario-generation)
      * Agents or tool use 
        * [ Testset Generation for Agents or Tool use cases  ](https://docs.ragas.io/en/latest/concepts/test_data_generation/agents/)
    * [ Feedback Intelligence  ](https://docs.ragas.io/en/latest/concepts/feedback/)
  * [ 🧪 Experimental  ](https://docs.ragas.io/en/latest/experimental/)
    * [ Tutorials  ](https://docs.ragas.io/en/latest/experimental/tutorials/)
      * [ Prompt  ](https://docs.ragas.io/en/latest/experimental/tutorials/prompt/)
      * [ RAG  ](https://docs.ragas.io/en/latest/experimental/tutorials/rag/)
      * [ Workflow  ](https://docs.ragas.io/en/latest/experimental/tutorials/workflow/)
      * [ Agent  ](https://docs.ragas.io/en/latest/experimental/tutorials/agent/)
    * [ Core Concepts  ](https://docs.ragas.io/en/latest/experimental/core_concepts/)
      * [ Metrics  ](https://docs.ragas.io/en/latest/experimental/core_concepts/metrics/)
      * [ Datasets  ](https://docs.ragas.io/en/latest/experimental/core_concepts/datasets/)
      * [ Experimentation  ](https://docs.ragas.io/en/latest/experimental/core_concepts/experimentation/)
  * [ 🛠️ How-to Guides  ](https://docs.ragas.io/en/latest/howtos/)
    * [ Customizations  ](https://docs.ragas.io/en/latest/howtos/customizations/)
      * General 
        * [ Customise models  ](https://docs.ragas.io/en/latest/howtos/customizations/customize_models/)
        * [ Run Config  ](https://docs.ragas.io/en/latest/howtos/customizations/_run_config/)
        * [ Caching  ](https://docs.ragas.io/en/latest/howtos/customizations/_caching/)
      * Metrics 
        * [ Modify Prompts  ](https://docs.ragas.io/en/latest/howtos/customizations/metrics/_modifying-prompts-metrics/)
        * [ Adapt Metrics to Languages  ](https://docs.ragas.io/en/latest/howtos/customizations/metrics/_metrics_language_adaptation/)
        * [ Write your own Metrics  ](https://docs.ragas.io/en/latest/howtos/customizations/metrics/_write_your_own_metric/)
        * [ Write your own Metrics - (advanced)  ](https://docs.ragas.io/en/latest/howtos/customizations/metrics/_write_your_own_metric_advanced/)
      * Testset Generation 
        * [ Non-English Testset Generation  ](https://docs.ragas.io/en/latest/howtos/customizations/testgenerator/_language_adaptation/)
        * [ Persona Generation  ](https://docs.ragas.io/en/latest/howtos/customizations/testgenerator/_persona_generator/)
        * [ Custom Single-hop Query  ](https://docs.ragas.io/en/latest/howtos/customizations/testgenerator/_testgen-custom-single-hop/)
        * [ Custom Multi-hop Query  ](https://docs.ragas.io/en/latest/howtos/customizations/testgenerator/_testgen-customisation/)
    * [ Applications  ](https://docs.ragas.io/en/latest/howtos/applications/)
      * Metrics 
        * [ Cost Analysis  ](https://docs.ragas.io/en/latest/howtos/applications/_cost/)
        * [ Evaluating Multi-turn Conversations  ](https://docs.ragas.io/en/latest/howtos/applications/evaluating_multi_turn_conversations/)
        * [ Evaluations with Vertex AI models  ](https://docs.ragas.io/en/latest/howtos/applications/vertexai_x_ragas/)
      * Testset Generation 
        * [ Single-hop Query Testset  ](https://docs.ragas.io/en/latest/howtos/applications/singlehop_testset_gen/)
      * Benchmarking 
        * [ Benchmarking Gemini models  ](https://docs.ragas.io/en/latest/howtos/applications/gemini_benchmarking/)
    * [ Integrations  ](https://docs.ragas.io/en/latest/howtos/integrations/)
      * [ Arize  ](https://docs.ragas.io/en/latest/howtos/integrations/_arize/)
      * [ Amazon Bedrock  ](https://docs.ragas.io/en/latest/howtos/integrations/amazon_bedrock/)
      * [ Haystack  ](https://docs.ragas.io/en/latest/howtos/integrations/haystack/)
      * [ Griptape  ](https://docs.ragas.io/en/latest/howtos/integrations/griptape/)
      * [ LangChain  ](https://docs.ragas.io/en/latest/howtos/integrations/langchain/)
      * [ LangGraph  ](https://docs.ragas.io/en/latest/howtos/integrations/_langgraph_agent_evaluation/)
      * [ LangSmith  ](https://docs.ragas.io/en/latest/howtos/integrations/langsmith/)
      * [ LlamaIndex RAG  ](https://docs.ragas.io/en/latest/howtos/integrations/_llamaindex/)
      * [ LlamaIndex Agents  ](https://docs.ragas.io/en/latest/howtos/integrations/llamaindex_agents/)
      * [ LlamaStack  ](https://docs.ragas.io/en/latest/howtos/integrations/llama_stack/)
      * [ R2R  ](https://docs.ragas.io/en/latest/howtos/integrations/r2r/)
      * [ Swarm  ](https://docs.ragas.io/en/latest/howtos/integrations/swarm_agent_evaluation/)
    * Migrations 
      * [ From v0.1 to v0.2  ](https://docs.ragas.io/en/latest/howtos/migrations/migrate_from_v01_to_v02/)
  * [ 📖 References  ](https://docs.ragas.io/en/latest/references/)
    * Core 
      * [ Prompt  ](https://docs.ragas.io/en/latest/references/prompt/)
      * [ LLMs  ](https://docs.ragas.io/en/latest/references/llms/)
      * [ Embeddings  ](https://docs.ragas.io/en/latest/references/embeddings/)
      * [ RunConfig  ](https://docs.ragas.io/en/latest/references/run_config/)
      * [ Executor  ](https://docs.ragas.io/en/latest/references/executor/)
      * [ Cache  ](https://docs.ragas.io/en/latest/references/cache/)
    * Evaluation 
      * [ Schemas  ](https://docs.ragas.io/en/latest/references/evaluation_schema/)
      * [ Metrics  ](https://docs.ragas.io/en/latest/references/metrics/)
      * [ evaluate()  ](https://docs.ragas.io/en/latest/references/evaluate/)
    * Testset Generation 
      * [ Schemas  ](https://docs.ragas.io/en/latest/references/testset_schema/)
      * [ Graph  ](https://docs.ragas.io/en/latest/references/graph/)
      * [ Transforms  ](https://docs.ragas.io/en/latest/references/transforms/)
      * [ Synthesizers  ](https://docs.ragas.io/en/latest/references/synthesizers/)
      * [ Generation  ](https://docs.ragas.io/en/latest/references/generate/)
    * [ Integrations  ](https://docs.ragas.io/en/latest/references/integrations/)
  * [ ❤️ Community  ](https://docs.ragas.io/en/latest/community/)


  * [ Evaluation  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluation)
    * [ Evaluating using a Non-LLM Metric  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-using-a-non-llm-metric)
    * [ Evaluating using a LLM based Metric  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-using-a-llm-based-metric)
    * [ Evaluating on a Dataset  ](https://docs.ragas.io/en/latest/getstarted/evals/#evaluating-on-a-dataset)
    * [ Want help in improving your AI application using evals?  ](https://docs.ragas.io/en/latest/getstarted/evals/#want-help-in-improving-your-ai-application-using-evals)
  * [ Up Next  ](https://docs.ragas.io/en/latest/getstarted/evals/#up-next)


# Evaluate a simple LLM application
The purpose of this guide is to illustrate a simple workflow for testing and evaluating an LLM application with `ragas`. It assumes minimum knowledge in AI application building and evaluation. Please refer to our [installation instruction](https://docs.ragas.io/en/latest/getstarted/install/) for installing `ragas`
## Evaluation
In this guide, you will evaluate a **text summarization pipeline**. The goal is to ensure that the output summary accurately captures all the key details specified in the text, such as growth figures, market insights, and other essential information.
`ragas` offers a variety of methods for analyzing the performance of LLM applications, referred to as [metrics](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/). Each metric requires a predefined set of data points, which it uses to calculate scores that indicate performance.
### Evaluating using a Non-LLM Metric
Here is a simple example that uses `BleuScore` score to score summary
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-1)fromragasimport SingleTurnSample
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-2)fromragas.metricsimport BleuScore
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-4)test_data = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-5)    "user_input": "summarise given text\nThe company reported an 8% rise in Q3 2024, driven by strong performance in the Asian market. Sales in this region have significantly contributed to the overall growth. Analysts attribute this success to strategic marketing and product localization. The positive trend in the Asian market is expected to continue into the next quarter.",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-6)    "response": "The company experienced an 8% increase in Q3 2024, largely due to effective marketing strategies and product adaptation, with expectations of continued growth in the coming quarter.",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-7)    "reference": "The company reported an 8% growth in Q3 2024, primarily driven by strong sales in the Asian market, attributed to strategic marketing and localized products, with continued growth anticipated in the next quarter."
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-8)}
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-9)metric = BleuScore()
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-10)test_data = SingleTurnSample(**test_data)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-0-11)metric.single_turn_score(test_data)

```

Output 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-1-1)0.137

```

Here we used:
  * A test sample containing `user_input`, `response` (the output from the LLM), and `reference` (the expected output from the LLM) as data points to evaluate the summary.
  * A non-LLM metric called [BleuScore](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/traditional/#bleu-score)


As you may observe, this approach has two key limitations:
  * **Time-Consuming Preparation:** Evaluating the application requires preparing the expected output (`reference`) for each input, which can be both time-consuming and challenging.
  * **Inaccurate Scoring:** Even though the `response` and `reference` are similar, the output score was low. This is a known limitation of non-LLM metrics like `BleuScore`. 


Info
A **non-LLM metric** refers to a metric that does not rely on an LLM for evaluation.
To address these issues, let's try an LLM-based metric.
### Evaluating using a LLM based Metric
**Choose your LLM**
[OpenAI](https://docs.ragas.io/en/latest/getstarted/evals/#__tabbed_1_1)[AWS](https://docs.ragas.io/en/latest/getstarted/evals/#__tabbed_1_2)[Google Cloud](https://docs.ragas.io/en/latest/getstarted/evals/#__tabbed_1_3)[Azure](https://docs.ragas.io/en/latest/getstarted/evals/#__tabbed_1_4)[Others](https://docs.ragas.io/en/latest/getstarted/evals/#__tabbed_1_5)
Install the langchain-openai package
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-2-1)pip
```

Ensure you have your OpenAI key ready and available in your environment.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-3-1)importos
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-3-2)os.environ["OPENAI_API_KEY"] = "your-openai-key"

```

Wrap the LLMs in `LangchainLLMWrapper` so that it can be used with ragas.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-1)fromragas.llmsimport LangchainLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-2)fromragas.embeddingsimport LangchainEmbeddingsWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-3)fromlangchain_openaiimport ChatOpenAI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-4)fromlangchain_openaiimport OpenAIEmbeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-5)evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-4-6)evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

```

Install the langchain-aws package
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-5-1)pip
```

Then you have to set your AWS credentials and configurations
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-1)config = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-2)    "credentials_profile_name": "your-profile-name",  # E.g "default"
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-3)    "region_name": "your-region-name",  # E.g. "us-east-1"
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-4)    "llm": "your-llm-model-id",  # E.g "anthropic.claude-3-5-sonnet-20241022-v2:0"
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-5)    "embeddings": "your-embedding-model-id",  # E.g "amazon.titan-embed-text-v2:0"
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-6)    "temperature": 0.4,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-6-7)}

```

Define your LLMs and wrap them in `LangchainLLMWrapper` so that it can be used with ragas.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-1)fromlangchain_awsimport ChatBedrockConverse
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-2)fromlangchain_awsimport BedrockEmbeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-3)fromragas.llmsimport LangchainLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-4)fromragas.embeddingsimport LangchainEmbeddingsWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-5)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-6)evaluator_llm = LangchainLLMWrapper(ChatBedrockConverse(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-7)    credentials_profile_name=config["credentials_profile_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-8)    region_name=config["region_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-9)    base_url=f"https://bedrock-runtime.{config['region_name']}.amazonaws.com",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-10)    model=config["llm"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-11)    temperature=config["temperature"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-12)))
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-13)evaluator_embeddings = LangchainEmbeddingsWrapper(BedrockEmbeddings(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-14)    credentials_profile_name=config["credentials_profile_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-15)    region_name=config["region_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-16)    model_id=config["embeddings"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-7-17)))

```

If you want more information on how to use other AWS services, please refer to the [langchain-aws](https://python.langchain.com/docs/integrations/providers/aws/) documentation.
Google offers two ways to access their models: Google AI Studio and Google Cloud Vertex AI. Google AI Studio requires just a Google account and API key, while Vertex AI requires a Google Cloud account. Use Google AI Studio if you're just starting out.
First, install the required packages (only the packages you need based on your choice of API):
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-8-1)# for Google AI Studio
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-8-2)pip[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-8-3)# for Google Cloud Vertex AI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-8-4)pip
```

Then set up your credentials based on your chosen API:
For Google AI Studio: 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-9-1)importos
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-9-2)os.environ["GOOGLE_API_KEY"] = "your-google-ai-key"  # From https://ai.google.dev/

```

For Google Cloud Vertex AI: 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-10-1)# Ensure you have credentials configured (gcloud, workload identity, etc.)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-10-2)# Or set service account JSON path:
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-10-3)os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/service-account.json"

```

Define your configuration:
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-1)config = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-2)    "model": "gemini-1.5-pro",  # or other model IDs
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-3)    "temperature": 0.4,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-4)    "max_tokens": None,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-5)    "top_p": 0.8,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-6)    # For Vertex AI only:
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-7)    "project": "your-project-id",  # Required for Vertex AI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-8)    "location": "us-central1",     # Required for Vertex AI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-11-9)}

```

Initialize the LLM and wrap it for use with ragas:
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-1)fromragas.llmsimport LangchainLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-2)fromragas.embeddingsimport LangchainEmbeddingsWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-4)# Choose the appropriate import based on your API:
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-5)fromlangchain_google_genaiimport ChatGoogleGenerativeAI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-6)fromlangchain_google_vertexaiimport ChatVertexAI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-7)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-8)# Initialize with Google AI Studio
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-9)evaluator_llm = LangchainLLMWrapper(ChatGoogleGenerativeAI(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-10)    model=config["model"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-11)    temperature=config["temperature"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-12)    max_tokens=config["max_tokens"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-13)    top_p=config["top_p"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-14)))
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-15)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-16)# Or initialize with Vertex AI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-17)evaluator_llm = LangchainLLMWrapper(ChatVertexAI(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-18)    model=config["model"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-19)    temperature=config["temperature"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-20)    max_tokens=config["max_tokens"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-21)    top_p=config["top_p"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-22)    project=config["project"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-23)    location=config["location"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-12-24)))

```

You can optionally configure safety settings:
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-1)fromlangchain_google_genaiimport HarmCategory, HarmBlockThreshold
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-2)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-3)safety_settings = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-4)    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-5)    # Add other safety settings as needed
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-6)}
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-7)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-8)# Apply to your LLM initialization
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-9)evaluator_llm = LangchainLLMWrapper(ChatGoogleGenerativeAI(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-10)    model=config["model"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-11)    temperature=config["temperature"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-12)    safety_settings=safety_settings,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-13-13)))

```

Initialize the embeddings and wrap them for use with ragas (choose one of the following):
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-1)# Google AI Studio Embeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-2)fromlangchain_google_genaiimport GoogleGenerativeAIEmbeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-4)evaluator_embeddings = LangchainEmbeddingsWrapper(GoogleGenerativeAIEmbeddings(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-5)    model="models/embedding-001",  # Google's text embedding model
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-6)    task_type="retrieval_document"  # Optional: specify the task type
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-14-7)))

```

```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-1)# Vertex AI Embeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-2)fromlangchain_google_vertexaiimport VertexAIEmbeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-4)evaluator_embeddings = LangchainEmbeddingsWrapper(VertexAIEmbeddings(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-5)    model_name="textembedding-gecko@001",  # or other available model
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-6)    project=config["project"],  # Your GCP project ID
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-7)    location=config["location"]  # Your GCP location
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-15-8)))

```

For more information on available models, features, and configurations, refer to: [Google AI Studio documentation](https://ai.google.dev/docs), [Google Cloud Vertex AI documentation](https://cloud.google.com/vertex-ai/docs), [LangChain Google AI integration](https://python.langchain.com/docs/integrations/chat/google_generative_ai), [LangChain Vertex AI integration](https://python.langchain.com/docs/integrations/chat/google_vertex_ai)
Install the langchain-openai package
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-16-1)pip
```

Ensure you have your Azure OpenAI key ready and available in your environment.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-1)importos
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-2)os.environ["AZURE_OPENAI_API_KEY"] = "your-azure-openai-key"
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-4)# other configuration
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-5)azure_config = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-6)    "base_url": "",  # your endpoint
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-7)    "model_deployment": "",  # your model deployment name
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-8)    "model_name": "",  # your model name
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-9)    "embedding_deployment": "",  # your embedding deployment name
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-10)    "embedding_name": "",  # your embedding name
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-17-11)}

```

Define your LLMs and wrap them in `LangchainLLMWrapper` so that it can be used with ragas.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-1)fromlangchain_openaiimport AzureChatOpenAI
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-2)fromlangchain_openaiimport AzureOpenAIEmbeddings
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-3)fromragas.llmsimport LangchainLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-4)fromragas.embeddingsimport LangchainEmbeddingsWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-5)evaluator_llm = LangchainLLMWrapper(AzureChatOpenAI(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-6)    openai_api_version="2023-05-15",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-7)    azure_endpoint=azure_config["base_url"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-8)    azure_deployment=azure_config["model_deployment"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-9)    model=azure_config["model_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-10)    validate_base_url=False,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-11)))
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-12)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-13)# init the embeddings for answer_relevancy, answer_correctness and answer_similarity
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-14)evaluator_embeddings = LangchainEmbeddingsWrapper(AzureOpenAIEmbeddings(
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-15)    openai_api_version="2023-05-15",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-16)    azure_endpoint=azure_config["base_url"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-17)    azure_deployment=azure_config["embedding_deployment"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-18)    model=azure_config["embedding_name"],
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-18-19)))

```

If you want more information on how to use other Azure services, please refer to the [langchain-azure](https://python.langchain.com/docs/integrations/chat/azure_chat_openai/) documentation.
If you are using a different LLM provider and using Langchain to interact with it, you can wrap your LLM in `LangchainLLMWrapper` so that it can be used with ragas.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-19-1)fromragas.llmsimport LangchainLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-19-2)evaluator_llm = LangchainLLMWrapper(your_llm_instance)

```

For a more detailed guide, checkout [the guide on customizing models](https://docs.ragas.io/en/latest/howtos/customizations/customize_models.md).
If you using LlamaIndex, you can use the `LlamaIndexLLMWrapper` to wrap your LLM so that it can be used with ragas.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-20-1)fromragas.llmsimport LlamaIndexLLMWrapper
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-20-2)evaluator_llm = LlamaIndexLLMWrapper(your_llm_instance)

```

For more information on how to use LlamaIndex, please refer to the [LlamaIndex Integration guide](https://docs.ragas.io/en/latest/howtos/integrations/_llamaindex.md).
If your still not able use Ragas with your favorite LLM provider, please let us know by by commenting on this [issue](https://github.com/explodinggradients/ragas/issues/1617) and we'll add support for it 🙂.
**Evaluation**
Here we will use [AspectCritic](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/aspect_critic/), which an LLM based metric that outputs pass/fail given the evaluation criteria.
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-1)fromragasimport SingleTurnSample
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-2)fromragas.metricsimport AspectCritic
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-3)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-4)test_data = {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-5)    "user_input": "summarise given text\nThe company reported an 8% rise in Q3 2024, driven by strong performance in the Asian market. Sales in this region have significantly contributed to the overall growth. Analysts attribute this success to strategic marketing and product localization. The positive trend in the Asian market is expected to continue into the next quarter.",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-6)    "response": "The company experienced an 8% increase in Q3 2024, largely due to effective marketing strategies and product adaptation, with expectations of continued growth in the coming quarter.",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-7)}
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-8)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-9)metric = AspectCritic(name="summary_accuracy",llm=evaluator_llm, definition="Verify if the summary is accurate.")
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-10)test_data = SingleTurnSample(**test_data)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-21-11)await metric.single_turn_ascore(test_data)

```

Output 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-22-1)1

```

Success! Here 1 means pass and 0 means fail
Info
There are many other types of metrics that are available in ragas (with and without `reference`), and you may also create your own metrics if none of those fits your case. To explore this more checkout [more on metrics](https://docs.ragas.io/en/latest/concepts/metrics/). 
### Evaluating on a Dataset
In the examples above, we used only a single sample to evaluate our application. However, evaluating on just one sample is not robust enough to trust the results. To ensure the evaluation is reliable, you should add more test samples to your test data.
Here, we’ll load a dataset from Hugging Face Hub, but you can load data from any source, such as production logs or other datasets. Just ensure that each sample includes all the required attributes for the chosen metric.
In our case, the required attributes are:  
- **`user_input`**: The input provided to the application (here the input text report).  
- **`response`**: The output generated by the application (here the generated summary).
For example
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-1)[
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-2)    # Sample 1
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-3)    {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-4)        "user_input": "summarise given text\nThe Q2 earnings report revealed a significant 15% increase in revenue, ...",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-5)        "response": "The Q2 earnings report showed a 15% revenue increase, ...",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-6)    },
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-7)    # Additional samples in the dataset
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-8)    ....,
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-9)    # Sample N
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-10)    {
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-11)        "user_input": "summarise given text\nIn 2023, North American sales experienced a 5% decline, ...",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-12)        "response": "Companies are strategizing to adapt to market challenges and ...",
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-13)    }
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-23-14)]

```

```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-1)fromdatasetsimport load_dataset
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-2)fromragasimport EvaluationDataset
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-3)eval_dataset = load_dataset("explodinggradients/earning_report_summary",split="train")
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-4)eval_dataset = EvaluationDataset.from_hf_dataset(eval_dataset)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-5)print("Features in dataset:", eval_dataset.features())
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-24-6)print("Total samples in dataset:", len(eval_dataset))

```

Output 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-25-1)Features in dataset: ['user_input', 'response']
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-25-2)Total samples in dataset: 50

```

Evaluate using dataset
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-26-1)fromragasimport evaluate
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-26-2)
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-26-3)results = evaluate(eval_dataset, metrics=[metric])
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-26-4)results

```

Output 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-27-1){'summary_accuracy': 0.84}

```

This score shows that out of all the samples in our test data, only 84% of summaries passes the given evaluation criteria. Now, **It s important to see why is this the case**.
Export the sample level scores to pandas dataframe
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-28-1)results.to_pandas()

```

Output 
```
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-29-1)    user_input                                          response                                            summary_accuracy
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-29-2)0   summarise given text\nThe Q2 earnings report r...   The Q2 earnings report showed a 15% revenue in...   1
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-29-3)1   summarise given text\nIn 2023, North American ...   Companies are strategizing to adapt to market ...   1
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-29-4)2   summarise given text\nIn 2022, European expans...   Many companies experienced a notable 15% growt...   1
[](https://docs.ragas.io/en/latest/getstarted/evals/#__codelineno-29-5)3   summarise given text\nSupply chain challenges ...   Supply chain challenges in North America, caus...   1

```

Viewing the sample-level results in a CSV file, as shown above, is fine for quick checks but not ideal for detailed analysis or comparing results across evaluation runs. 
### Want help in improving your AI application using evals?
In the past 2 years, we have seen and helped improve many AI applications using evals. 
We are compressing this knowledge into a product to replace vibe checks with eval loops so that you can focus on building great AI applications.
If you want help with improving and scaling up your AI application using evals.
🔗 Book a [slot](https://bit.ly/3EBYq4J) or drop us a line: founders@explodinggradients.com.
[![](https://docs.ragas.io/en/latest/_static/ragas_app.gif)](https://docs.ragas.io/en/latest/_static/ragas_app.gif)
## Up Next
  * [Evaluate a simple RAG application](https://docs.ragas.io/en/latest/getstarted/rag_eval/)

April 24, 2025 April 5, 2025 GitHub [ ![shahules786](https://avatars.githubusercontent.com/u/25312635?v=4&size=72) ](https://github.com/shahules786 "@shahules786") [ ![web-flow](https://avatars.githubusercontent.com/u/19864447?v=4&size=72) ](https://github.com/web-flow "@web-flow") [ ![carlosgsouza](https://avatars.githubusercontent.com/u/2100387?v=4&size=72) ](https://github.com/carlosgsouza "@carlosgsouza") [ ![iamarunbrahma](https://avatars.githubusercontent.com/u/6504730?v=4&size=72) ](https://github.com/iamarunbrahma "@iamarunbrahma") [ +1 ](https://github.com/explodinggradients/ragas/blob/master/docs/getstarted/evals.md)
[ Previous  Installation  ](https://docs.ragas.io/en/latest/getstarted/install/) [ Next  Evaluate a simple RAG  ](https://docs.ragas.io/en/latest/getstarted/rag_eval/)
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)
