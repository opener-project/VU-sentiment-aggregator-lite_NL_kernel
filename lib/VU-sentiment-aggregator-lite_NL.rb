module Opener
   module Kernel
     module VU
       module Sentiment-Aggregator
    	 module lite
    	   module NL
      		VERSION = "0.0.1"

      		class Configuration
        		CORE_DIR    = File.expand_path("../core", File.dirname(__FILE__))
        		KERNEL_CORE = CORE_DIR+'/SentimentAggregatorLite.py'
      		end

    	  end
    	end
      end
    end
  end
end

KERNEL_CORE=Opener::Kernel::VU::Sentiment-Aggregator::lite::NL::Configuration::KERNEL_CORE
